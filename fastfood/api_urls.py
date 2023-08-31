from django.urls import path
from .views import (
    MenuAPIView,
    MenuItemDeleteView,
    MenuItemUpdateView,
    MenuItemCreateView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ---------------------These api's are ste up for the REACT app CRUD and JWT tokens

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('menu/', MenuAPIView.as_view(), name='menu-list'),
    path('menu/items/create/', MenuItemCreateView.as_view(), name='menu-item-create'),
    path('menu/item/<int:pk>/delete/', MenuItemDeleteView.as_view(), name='menu-item-delete'),
    path('menu/item/<int:pk>/update/', MenuItemUpdateView.as_view(), name='menu-item-update'),
]
