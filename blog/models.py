# Create your models here.
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={
            'slug': self.slug
        })


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateField(default=timezone.now)
    comment = models.TextField(null=True, default="Commented Dilip")

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)


class Dilip(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    enquiry = models.CharField(max_length=50)

    def __str__(self):
        return self.name

