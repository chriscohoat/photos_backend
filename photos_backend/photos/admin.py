from models import *
from django.contrib import admin

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Album, AlbumAdmin)