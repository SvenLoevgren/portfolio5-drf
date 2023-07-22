from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fastfood.urls')),
    path('api/', include('fastfood.api_urls')),  # API URLs
    path('accounts/', include('allauth.urls')),
]
