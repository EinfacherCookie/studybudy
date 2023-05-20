from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# # <- Cooming Soon ;D

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200) # Der Name des Rooms
    description = models.TextField(null=True, blank=True) # Eine Beschreibung die auch leer sein darf
    #participants = 
    updated = models.DateTimeField(auto_now=True) # Updates on Save / Change
    created = models.DateTimeField(auto_now_add=True) # Set intial Timestamp on creation
    
    class Meta:
        ordering = ['-updated', '-created']
        #-updated = from newest to oldest
        #updated = from oldest to newest 
    
    def __str__ (self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    #Wenn der Room (Parent) gelöscht wird dann wird die Message ebenfalls gelöscht
    #geht auch mit models.SET_NULL -> Dann wird nur die Beziehung gelöscht, aber nicht die Nachricht
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # Updates on Save / Change
    created = models.DateTimeField(auto_now_add=True) # Set intial Timestamp on creation
    
    def __str__(self):
        return self.body[0:50]