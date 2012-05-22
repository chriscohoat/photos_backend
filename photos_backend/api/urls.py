from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from handlers import CreateAlbumHandler

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import urlquote

auth = HttpBasicAuthentication(realm="API Realm")
with_auth = { 'authentication': auth }
no_auth = {'authentication': None}

class CsrfExemptResource(Resource):
    """A Custom Resource that is csrf exempt"""
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

create_album = CsrfExemptResource(handler=CreateAlbumHandler, **no_auth)

urlpatterns = patterns('',
                       url(r'^create/album/$', create_album),
                       )