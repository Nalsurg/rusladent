from django.db import models

# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=300)
	resourceId = models.CharField(max_length=300)
	start_time = models.CharField(max_length=300)
	end_time = models.CharField(max_length=300)