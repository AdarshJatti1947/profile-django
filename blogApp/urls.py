from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('blog', views.blog_page),
    path('my-url/', views.my_function, name='my_function'),



]