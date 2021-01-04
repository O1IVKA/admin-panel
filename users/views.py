from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Userc
from .forms import ProfileCreateChange, LoginForm


class LogIn(LoginView):
    """view for logging in"""
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('create')

class LogOut(LogoutView):
    """view for logging out"""
    next_page = '/'


class Reg(CreateView):
    """view for registration"""
    model = Userc
    template_name = 'reg.html'
    success_url = reverse_lazy('create')
    success_msg = 'Пользователь создан'
    form_class = ProfileCreateChange

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid

