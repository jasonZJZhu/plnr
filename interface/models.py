from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Challenge(models.Model):
	title = models.CharField(max_length=100)
	# Icon
	icon_url = models.ImageField(default="default.jpg", upload_to="icons")
	# Progress Bar in %
	progress = models.IntegerField(default=0)
	description = models.TextField()
	deadline = models.DateField()

	def __str__(self):
		return self.title