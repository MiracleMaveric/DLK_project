from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('blog/', include('blog.urls')),
    path('catalog/', include('catalog.urls')),
    path('toys/', include('toys.urls')),
    path('ContactUs/', include('ContactUs.urls')),
    path('core/', include('core.urls')),
]
