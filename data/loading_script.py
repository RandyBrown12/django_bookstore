from io import StringIO
import psycopg2
import pandas as pd
import json

def load_csv_data_to_postgres():
    with open('psql_info.json', 'r') as file:
        db_info = json.load(file)

    books_dataset = pd.read_csv('data/books.csv')
    authors_dataset = pd.read_csv('data/authors.csv')
    publishers_dataset = pd.read_csv('data/publishers.csv')

    conn = psycopg2.connect(**db_info)
    cursor = conn.cursor()

    # Insert data into authors table
    authors_dataset_trimmed = authors_dataset.drop(columns=['Title'])

    buffer = StringIO()
    authors_dataset_trimmed.to_csv(buffer, index=False)
    buffer.seek(0)
    
    cursor.copy_expert("""COPY AUTHORS (AUTHOR_FIRST_NAME, AUTHOR_LAST_NAME) FROM STDIN WITH CSV HEADER""", buffer)

    # Insert data into publishers table
    publishers_dataset_trimmed = publishers_dataset.drop(columns=['Title'])

    buffer = StringIO()
    publishers_dataset_trimmed.to_csv(buffer, index=False)
    buffer.seek(0)

    cursor.copy_expert("""COPY PUBLISHERS (PUBLISHER, PUBLISHER_DATE) FROM STDIN WITH CSV HEADER""", buffer)

    # Insert data into books table
    for _, row in books_dataset.iterrows():

        binary_image_path = row.get('Image_Location', None)

        if binary_image_path:
            with open(f"img/{binary_image_path}", 'rb') as image_file:
                binary_image_data = image_file.read()

        cursor.execute("""
            INSERT INTO BOOKS (TITLE, CATEGORY, LANGUAGE, PAGE_COUNT, DESCRIPTION, BOOK_COUNT, PRICE, IMAGE)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (row['Title'], row['Category'], row['Language'], row['Page_Count'], row['Description'], row['Book_Count'], row['Price'], binary_image_data))

    # Insert data into authors_books table
    for _, author in authors_dataset.iterrows():
        cursor.execute("""
                INSERT INTO BOOK_TO_AUTHOR (BOOK_ID, AUTHOR_ID)
                SELECT B.BOOK_ID, A.AUTHOR_ID
                FROM BOOKS B, AUTHORS A
                WHERE B.TITLE = %s AND A.AUTHOR_FIRST_NAME = %s AND A.AUTHOR_LAST_NAME = %s
                """, (author['Title'], author['Author_First_Name'], author['Author_Last_Name']))
        
    # Insert data into publishers_books table
    for _, publisher in publishers_dataset.iterrows():
        cursor.execute("""
                INSERT INTO BOOK_TO_PUBLISHER (BOOK_ID, PUBLISHER_ID)
                SELECT B.BOOK_ID, P.PUBLISHER_ID
                FROM BOOKS B, PUBLISHERS P
                WHERE B.TITLE = %s AND P.PUBLISHER = %s
                """, (publisher['Title'], publisher['Publisher']))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("Data loading script started.")
    load_csv_data_to_postgres()
    print("Data loading script executed successfully.")