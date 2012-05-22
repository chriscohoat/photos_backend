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