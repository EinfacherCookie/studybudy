from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #Index Page
    
    path('room/<str:pk>/', views.room, name="room")
    #"str" <- String; ":pk" <- Primary Key (Wert der Übergeben wird)
]