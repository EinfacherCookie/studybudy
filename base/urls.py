from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #Index Page
    
    path('room/<str:pk>/', views.room, name="room"),
    #"str" <- String; ":pk" <- Primary Key (Wert der Übergeben wird)
    
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete_room/<str:pk>/', views.deleteRoom, name="delete-room"),
]