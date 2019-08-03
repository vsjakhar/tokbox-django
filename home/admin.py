from django.contrib import admin
from .models import *

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
	list_display = ['user',  'title', 'slug', 'session', 'token', 'timestamp', 'status']
	search_fields = ['user__username', 'title', 'slug', 'session', 'token']
	readonly_fields = ('session', 'token', 'track', 'timestamp', 'status')
	actions = None

admin.site.register(Room, RoomAdmin)
