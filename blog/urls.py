# from django.urls import path
# from .views import post_list
#
# urlpatterns = [
#     path('', views/post_list, name='post_list'),
# ]


from django.urls import path
from .views import PostList, PostDetail,post_new,post_edit

urlpatterns = [
    path('', PostList.as_view()),
    path('<slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<slug>/edit/', post_edit, name='post_edit'),
]
