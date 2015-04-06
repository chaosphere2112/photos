from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .models import Photo

def view_photos(request):
	photos = Photo.objects.all()
	return render(request, "photo_uploader/display.html", RequestContext(request, {"photos": photos}))