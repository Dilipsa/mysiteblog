from django.contrib import admin

# Register your models here.
from .models import Post, Name


admin.site.register(Post)
admin.site.register(Name)
