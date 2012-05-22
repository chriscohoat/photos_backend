from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title
    
class Photo(models.Model):
    album = models.ForeignKey(Album,related_name='photos')
    relative_path = models.CharField(max_length=500,null=True)
    def __unicode__(self):
        return '%s - %s' % (self.album,self.relative_path)