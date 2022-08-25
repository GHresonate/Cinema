from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_admin/', include('my_admin.urls')),
    path('pages/', include('pages_app.urls')),
    path('cinema/', include('cinema_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
