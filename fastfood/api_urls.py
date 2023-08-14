from django.urls import path
from .views import MenuAPIView, MenuItemDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('menu/', MenuAPIView.as_view(), name='menu-list'), # for REACT app
    path('menu/item/<item_ids>/delete/', MenuItemDeleteView.as_view(), name='menu-item-delete'),
]
