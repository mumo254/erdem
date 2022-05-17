from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/<blogs_id>', views.comments, name='comments'),
]
