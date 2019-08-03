from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from opentok import OpenTok

# Create your models here.

status = (("Draft","Draft"),("Schedule","Schedule"),("Active","Active"),("Inactive","Inactive"),("Delete","Delete"))

class Room(models.Model):
	"""docstring for Room"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=160)
	slug = AutoSlugField(populate_from=['title'], unique=True, editable=True)
	session = models.CharField(max_length=160, blank=True, editable=False)
	token = models.CharField(max_length=360, blank=True, editable=False)
	track = models.TextField(blank=True, editable=False)
	timestamp = models.DateTimeField(auto_now=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	def save(self, *args, **kwargs):
		if len(self.token)<10:
			opentok = OpenTok(settings.TOK_KEY, settings.TOK_SECRET)
			session = opentok.create_session()
			self.token = session.generate_token()
			self.session = session.session_id
		super(Room, self).save(*args, **kwargs)

	def __str__(self):
		return (self.title)
		
