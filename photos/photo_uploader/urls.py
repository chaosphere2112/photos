from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', view_photos),
    url(r'^upload_photos$', upload_photos),
    url(r'^upload$', upload_action),
    url(r'^save_caption$', set_captions),
    url(r'^photo/([^/]+)$', photo),
]
