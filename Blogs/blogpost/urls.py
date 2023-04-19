from . import views
from django.urls import path

urlpatterns = [
    path('', views.postLists.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contactus'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
