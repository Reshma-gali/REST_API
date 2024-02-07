from django.contrib import admin

# Register your models here.
from Books.models import Books

admin.site.register(Books)
