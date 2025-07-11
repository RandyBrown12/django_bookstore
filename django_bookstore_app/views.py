import base64
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django_bookstore_app.models import BookInformation, CartInformation
from django.http import HttpResponse

# Create your views here.
@login_required
def books_view(request):
    """
    Render the books page, displaying a list of books.
    """    
    # Fetch books from the database (assuming a Books model exists)
    books = BookInformation.objects.all()

    for book in books:
        # Convert binary image data to a displayable format if needed
        raw_bytes = bytes(book.image)
        book.image = base64.b64encode(raw_bytes).decode('utf-8')

    return render(request, 'index.html', {'books': books})

@require_POST
@login_required
def add_to_cart_API(request):
    """
    Handle adding a book to the cart.
    """
    try:
        request_body = request.body.decode('utf-8')

        # Assuming the request body is a JSON string
        import json
        try:
            book_id = json.loads(request_body)['book_id']
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON format", status=400)
        if not book_id:
            return HttpResponse("No book_id provided", status=400)
        
        user_id = request.user.id
        cart_item, created = CartInformation.objects.get_or_create(
            customer_id=user_id,
            book_id=book_id,
            defaults={'quantity': 1}
        )

        if not created:
            # TODO: Add logic to handle case where quantity exceeds available stock
            cart_item.quantity += 1
            cart_item.save()

    except Exception as e:
        # Handle any errors that occur during the process
        return HttpResponse(f"Error adding item {book_id} to cart: {str(e)}", status=500)

    return HttpResponse("OK")

@login_required
def order_view(request):
    """
    Render the order page, displaying a list of books available for order.
    """
    return render(request, 'order.html')

def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    return redirect('login_view')

def login_view(request):
    """
    Render the login page.
    """
    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('books_view')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def signup_view(request):
    """
    Render the signup page.
    """
    if request.method == 'POST':
        # Handle signup logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add user creation logic here
        user = User.objects.create_user(username=username, password=password)
        user.save()
        # Redirect to login or index page after successful signup
        return redirect('login_view')
    else:
        return render(request, 'signup.html')