from django.urls import path
from django_bookstore_app.views import books_view, login_view, logout_view, signup_view, order_view, add_to_cart_API
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='root_redirect'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('books/', books_view, name='books_view'),
    path('logout/', logout_view, name='logout_view'),
    path('order/', order_view, name='order_view'),
    path('cart/add', add_to_cart_API, name='add_to_cart_API'),
]