from piston.handler import BaseHandler
from piston.utils import rc, throttle
import json
from photos_backend.photos.models import *

class ListAlbumHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Album
    fields = ('id','title',('photos',('id','relative_path',)))
    
    def read(self,request):
        
        try:
            title = request.GET['album_title']
        except:
            title = None
        
        if not title:
            return {'error':'No title specified.'}
        else:
            try:
                album = Album.objects.get(title=title)
            except:
                return {'error':'Album not found.'}
            return {'album':album}

class RemoveFromAlbumHandler(BaseHandler):
    allowed_methods = ('POST')
    
    def create(self,request):
        
        try:
            title = request.POST['album_title']
            id = request.POST['id']
        except:
            return rc.BAD_REQUEST
        
        try:
            album = Album.objects.get(title=title)
        except:
            return {'error':'Album not found.'}
        
        try:
            photo = Photo.objects.get(album=album,id=id)
        except:
            return {'error':'Photo not found.'}
        
        success = False
        try:
            photo.delete()
            success = True
        except:
            pass
        
        return {'success':success}

class AddToAlbumHandler(BaseHandler):
    allowed_methods = ('POST')
    
    def create(self,request):
        
        try:
            title = request.POST['album_title']
            filename = request.POST['filename']
        except:
            return rc.BAD_REQUEST
        
        try:
            album = Album.objects.get(title=title)
        except:
            return {'error':'Album not found.'}
        
        #Save to get unique ID
        photo = Photo()
        photo.album = album
        photo.save()
        
        photo.relative_path = '/static/%s_%s' % (photo.id,filename)
        photo.save()
        
        return {'album':album}

class CreateAlbumHandler(BaseHandler):
    allowed_methods = ('POST')
    model = Album
    fields = ('id','title',('photos',))
    
    def create(self,request):
        
        try:
            title = request.POST['album_title']
        except:
            return rc.BAD_REQUEST
        
        album,created = Album.objects.get_or_create(title=title)
        
        return {'created':created,'album':album}