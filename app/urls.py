from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogDetails/<blogs_id>', views.blogDetails, name='blogDetails'),
    path('blogDetail/', views.blogDetail, name='blogDetail'),
    path('comments/<blogs_id>', views.comments, name='comments'),
]
