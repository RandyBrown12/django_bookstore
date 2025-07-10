from django.contrib import admin
from .models import Books, Customers, Orders, OrderBooks, Publishers, Authors, BookToAuthor, BookToPublisher, BookInformation, CartInformation
# Register your models here.

admin.site.register(Books)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(OrderBooks)
admin.site.register(Publishers)
admin.site.register(Authors)
admin.site.register(BookToAuthor)
admin.site.register(BookToPublisher)
admin.site.register(BookInformation)
admin.site.register(CartInformation)