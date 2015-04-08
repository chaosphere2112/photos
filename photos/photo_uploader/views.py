from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Photo
import json
from django.utils.text import get_valid_filename

def view_photos(request):
	try:
		if request.user.is_staff:
			photos = Photo.objects.all()
		else:
			photos = Photo.objects.filter(display=True)
		return render(request, "photo_uploader/display.html", RequestContext(request, {"photos": photos}))
	except Photo.DoesNotExist:
		return render(request, "photo_uploader/display.html", RequestContext(request, {"photos": []}))

def upload_photos(request):
	if request.user.is_staff == False:
		return HttpResponse("Access denied")

	return render(request, "photo_uploader/upload.html", RequestContext(request))

def set_captions(request):
	if request.method == "POST":
		for key in request.POST.keys():
			if "file_name_" == key[:len("file_name_")]:
				file_num = key[len("file_name_"):]
				file_name = get_valid_filename(request.POST[key])
				file_caption = request.POST["caption_%s" % file_num]
				fileobj = Photo.objects.get(photo=file_name)
				fileobj.caption = file_caption
				fileobj.display = True
				fileobj.save()
		return HttpResponseRedirect("/")
	else:
		return error()

def upload_action(request):
	if request.method == "POST":
		for key in request.FILES.keys():
			new_photo = Photo(photo=request.FILES[key])
			new_photo.save()
		message = { "status": "success"}
		return HttpResponse(json.dumps(message), content_type="application/json")
	elif request.method == "DELETE":
		try:
			req_data = json.loads(request.body)
			if "filename" in req_data:
				f = get_valid_filename(req_data["filename"])
				files = Photo.objects.filter(photo=f)
				for fileobj in files:
					if fileobj.display == False:
						fileobj.delete()
				message = {"status": "success"}
				return HttpResponse(json.dumps(message), content_type="application/json")
			else:
				return error()
		except ValueError:
			return error()
	return error()


def error(message=None, status=400):
	if message is not None:
		response = HttpResponse(message)
	else:
		response = HttpResponse()

	response.status_code = status
	return repsonse