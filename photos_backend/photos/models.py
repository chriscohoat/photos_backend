from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    
class Photo(models.Model):
    album = models.ForeignKey(Album,related_name='photos')
    relative_path = models.CharField(max_length=500,null=True)