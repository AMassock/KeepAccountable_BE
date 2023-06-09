from django.contrib import admin
from django.urls import path   
from . import views 
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]