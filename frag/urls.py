
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', include('mainpage.urls')),
    path('users_', include('users.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
