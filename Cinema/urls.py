from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [path('i18n/', include('django.conf.urls.i18n')),]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('my_admin/', include('my_admin.urls')),
    path('pages/', include('pages_app.urls')),
    path('', include('cinema_app.urls')),
    path('user/', include('user_app.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
