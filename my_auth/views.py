from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from .forms import LoginForm, SignupForm, PasswordResetForm, SetPasswordForm

User = get_user_model()

class LoginView(auth_views.LoginView):
    template_name = 'my_auth/signin.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('my_auth_success')

class SignupView(FormView):
    template_name = 'my_auth/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('my_auth_signin')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

def success_view(req):
    return render(req, 'my_auth/success.html')
