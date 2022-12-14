from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls')),
    path('', include('auth_app.urls')),
    path('auth1/', include('djoser.urls')),
    path('', include('send_email.urls'))
    # path('auth2/', include('djoser.urls.authtoken')),
    # path('auth3/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
