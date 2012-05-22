from piston.handler import BaseHandler
from piston.utils import rc, throttle
import json

class CreateAlbumHandler(BaseHandler):
    allowed_methods = ('POST')
    #model = ModelHere
    #fields = ('field1',)
    
    def create(self,request):
        print "POSTING"
        print 'POST MATERIAL : ',request.POST

