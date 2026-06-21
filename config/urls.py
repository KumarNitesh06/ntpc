from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Accounts App
    path('', include('accounts.urls')),

    # Assets App
    path('assets/', include('assets.urls')),

    # Complaints App
    path('complaints/', include('complaints.urls')),
]

# Media Files (Photo Uploads)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )