from django.contrib import admin

# Register your models here.
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	pass
