from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths Core
    path('', include('core.urls')),

    # Paths Studio
    path('studio/', include('studio.urls')),

    # Paths Texts
    path('texts/', include('texts.urls')),

    # Path Admin
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Kimmi Records"

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
