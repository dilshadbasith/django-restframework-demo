from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='user_auth')

urlpatterns = [
    path('', include(router.urls)),
    # JWT token obtain and refresh
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
