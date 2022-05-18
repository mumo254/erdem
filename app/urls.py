from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogDetails/<blogs_id>', views.blogDetails, name='blogDetails'),
    path('blogDetail/', views.blogDetail, name='blogDetail'),
    path('comments/<blogs_id>', views.comments, name='comments'),
    path('blogsDetails/<blogs_id>', views.blogsDetails, name='blogsDetails'),
    path('blogsDetail/', views.blogsDetail, name='blogsDetail'),
    path('comment/<blogs_id>', views.comment, name='comment'),
]
