# listings/admin.py

from django.contrib import admin

from listings.models import Band

from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'year')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, SongAdmin)

# Register your models here.
