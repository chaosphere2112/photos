from django.db import models

# Create your models here.
class Photo(models.Model):
	photo   = models.ImageField(height_field="height", width_field="width")
	caption = models.TextField(null=True, blank=True)
	width   = models.IntegerField(null=True, blank=True)
	height  = models.IntegerField(null=True, blank=True)
	display = models.BooleanField(default=False)