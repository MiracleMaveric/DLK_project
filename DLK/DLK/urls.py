from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('blog/', include('blog.urls')),
    path('catalog/', include('catalog.urls')),
    path('toys/', include('toys.urls')),
    path('ContactUs/', include('ContactUs.urls')),
    path('core/', include('core.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/img/empty_avatar.png')),
    path('post/', include('post.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)