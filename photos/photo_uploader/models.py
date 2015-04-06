from django.db import models

# Create your models here.
class Photo(models.Model):
	photo = models.ImageField(height_field="height", width_field="width")
	caption = models.TextField()
	width = models.IntegerField()
	height = models.IntegerField()