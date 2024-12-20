from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='my_auth_signup'),
    path('signin/', LoginView.as_view(), name='my_auth_signin'),
    path('signout/', LogoutView.as_view(next_page='my_auth_success'), name='my_auth_signout'),
]
