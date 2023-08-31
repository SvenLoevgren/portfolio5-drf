from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # drf app urls
    path('', include('fastfood.urls')),
    # react app urls
    path('api/', include('fastfood.api_urls')),
    path('accounts/', include('allauth.urls')),
]
