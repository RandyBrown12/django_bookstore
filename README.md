# Online Bookstore Project from EMRTS

This project simulate an e-commerce project where users can purchase books.

## How to setup the project.

Developers can run the project by performing the following steps.

1. Create a Virtual Environment:
   `uv venv .venv`
2. Access the Virtual Environment:
   Windows: `.venv/Scripts/activate`
3. Install required packages:
   `uv pip install -r requirements.txt`
4. Rename psql_info_template.json to psql_info.json and insert database information:

You are now to ready to run the project.

### How to run the project

* For Development:
  `py manage.py runserver`
* For Deployment with Gunicorn:

  > Before Deploying:
  >
  > Check and fix errors: `py manage.py check --deploy`
  >
  > Place gunicorn.service file in this repo to /etc/systemd/system
  >
  > Run gunicorn: `sudo systemctl enable gunicorn`
  >
  > Install nginx and place django_bookstore_reverse_proxy.conf to /etc/nginx/sites-available
  >
  > In /etc/nginx/sites-enabled, perform a link to the place django_bookstore_reverse_proxy.conf and also delete the link pointing to default.
  >
  > Ex: `sudo ln -s /etc/nginx/sites-available/django-bookstore-reverse-proxy.conf /etc/nginx/sites-enabled/`
  >
  > Install certbot to perform HTTPS
  >
  > `sudo apt install certbot python3-certbot-nginx`
  >
  > `sudo certbot --nginx`
  >

  1. Update settings.py in django_bookstore

  ```
  SECRET_KEY = <generate_random_key>
  DEBUG = False
  ALLOWED_HOSTS = ["<domain_name>"]
  ```

  2. Create a tailwind build to the project

  > Note: Make sure NPM_PATH is specified in settings.py and also you have run `npm install` inside static_src directory in theme.
  > `python manage.py tailwind build`
  > `python manage.py collectstatic`
  >

  3. Perform migrations to database
     `python manage.py makemigrations django_bookstore_app`
     `python manage.py migrate`

  > Note: Create the views, functions, and triggers located in database.sql to postgres database
  >

  4. Load data into database inside data directory
     `python data/loading_script.py`

You are now ready to use the project.

### Running this on Ansible

Prerequisites: Docker, ssh-keygen (Windows 10 & Later includes OpenSSH)

1. Change directory to the ansible folder:
   `cd ansible`

2. Add a psql_info.json in the django_bookstore directory and put it into this directory.
   `cp ../psql_info.json .`

3. Create a ssh-keygen into the ansible directory.
   `ssh-keygen -t ed22519 -C "<email_here>"`

4. Start the containers in the background using Docker Compose:
   `docker compose up --build -d`

> Note: You can stop containers using `docker compose down`

4. Access the ansible-control container in exec mode for the next two commands:
   `docker compose exec -it ansible-control /bin/bash`

5. Initialize SSH fingerprints by running a ping test (this will prompt you to accept SSH keys for the other containers):
   `ansible all -m ping -i /ansible/inventory.ini --private-key=~/.ssh/authorized_keys`
> Note: It will ask if you want to continue connecting, type `yes`. Type `yes` again for the other container.

6. Run the Ansible playbook to configure the environment:
   `ansible-playbook -i /ansible/inventory.ini /ansible/playbook.yml --private-key=~/.ssh/authorized_keys`

7. Access the application on your host machine at: `http://localhost:20000`

### URLs

Login: `https:<domain_name>/login/`

Sign Up: `https:<domain_name>/signup/`
