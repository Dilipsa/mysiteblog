from django.urls import path
from .views import post_list, post_detail, post_new,post_edit, postComment

app_name="blog"
urlpatterns = [
    path('', post_list),
    path('<slug>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<slug>/edit/', post_edit, name='post_edit'),

    path('postComment/<slug>/', postComment, name='postComment'),
]
