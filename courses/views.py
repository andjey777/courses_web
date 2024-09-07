from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView

from courses.forms import UserLoginForm, UserRegisterForm

# Create your views here.

class IndexView(generic.View):
    pass


class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = "courses/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy("courses:index")

class RegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'courses/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('courses:index')

def Logout_View(request):
    logout(request)
    return redirect("courses:index")

