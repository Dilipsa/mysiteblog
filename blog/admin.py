from django.contrib import admin

# Register your models here.
from .models import Post, BlogComment, Category, Dilip


admin.site.register((Post, BlogComment, Category, Dilip))
