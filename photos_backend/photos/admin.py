from models import *
from django.contrib import admin

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title',)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','album','relative_path',)
    
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)