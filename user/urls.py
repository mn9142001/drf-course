from .views import SignupView, JWTLoginView, PasswordChangeView, PasswordResetVerifyView, PasswordResetSendView, PasswordResetConfirmView, UserBlockView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView


password_urls = [
    path('reset/send/', PasswordResetSendView.as_view()),
    path('reset/verify/', PasswordResetVerifyView.as_view()),
    path('reset/change/', PasswordResetConfirmView.as_view()),
    path('change/', PasswordChangeView.as_view()),
]

auth_urls = [
    path('token/refresh/', TokenRefreshView.as_view()),
    path('signup/', SignupView.as_view()),
    path('login/', JWTLoginView.as_view()),
    path('password/', include(password_urls))
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('utils/block/', UserBlockView.as_view()),
]
