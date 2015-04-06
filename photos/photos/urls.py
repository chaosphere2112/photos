from django.conf.urls import include, url
from django.contrib import admin
import photo_uploader.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'photos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photos/', photo_uploader.views.view_photos)
]
