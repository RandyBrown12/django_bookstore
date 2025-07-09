import base64
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django_bookstore_app.models import BookInformation

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