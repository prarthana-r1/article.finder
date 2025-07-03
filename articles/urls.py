from django.urls import path
from . import views

urlpatterns = [
      path('', views.article_list, name='home'),  # use name='home' here
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
