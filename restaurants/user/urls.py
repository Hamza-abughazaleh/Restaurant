from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user import views

urlpatterns = [
    # Your URLs...
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='api-login'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='api-login-refresh'),
    path('employees/', views.CandidatesCreateAPIView.as_view(), name='employees-registration'),
]
