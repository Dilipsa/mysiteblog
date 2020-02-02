from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.shortcuts import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={
        'slug' : self.slug
        })


class Language(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Framework(models.Model):
    name=models.CharField(max_length=20)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Character(models.Model):
    name=models.CharField(max_length=20)
    movies= models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class Name(models.Model):
    name=models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("name-detail",kwargs={
        'slug' : self.slug
        })
