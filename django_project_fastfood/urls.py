from django.contrib import admin
from django.urls import include, path
from fastfood.views import CustomLoginView, CustomSignupView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fastfood.urls')),
    path('api/', include('fastfood.api_urls')),  # API URLs
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),  # Custom sign-up view
    path('accounts/logout/', CustomLogoutView.as_view(), name='account_logout'),  # Custom logout view
    path('accounts/', include('allauth.urls')),  # Allauth URLs
]
