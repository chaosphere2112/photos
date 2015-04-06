from django.conf.urls import include, url
from django.contrib import admin
import photo_uploader.urls
from photo_uploader.views import view_photos

urlpatterns = [
    # Examples:
    # url(r'^$', 'photos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^photos/', include(photo_uploader.urls)),
    url(r'^$', view_photos),
]
