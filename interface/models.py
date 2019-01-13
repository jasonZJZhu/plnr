from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Challenge(models.Model):
	title = models.CharField(max_length=100)
	# Icon
		# icon = models
	# Progress Bar
		# progress = models
	description = models.TextField()
	deadline = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title