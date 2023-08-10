from django.urls import path
from .views import BookingListCreateAPIView, BookingDetailAPIView, MenuAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('menu/cart', MenuAPIView.as_view(), name='menu-list'), # for REACT app
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'), # for REACT app
]
