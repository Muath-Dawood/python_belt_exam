from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, SignupView, PasswordResetView, SetPasswordView, success_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='my_auth_signup'),
    path('signin/', LoginView.as_view(), name='my_auth_signin'),
    path('signout/', LogoutView.as_view(next_page='my_auth_success'), name='my_auth_signout'),
    path('success/', success_view, name='my_auth_success'),
    path('reset/', PasswordResetView.as_view(), name='my_auth_password_reset'),
    path('reset/<uidb64>/<token>/', SetPasswordView.as_view(), name='my_auth_password_reset_confirm'),
]
