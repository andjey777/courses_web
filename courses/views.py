from django.contrib.auth import (
    login,
    logout,
)
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from courses.forms import (
    UserLoginForm,
    UserRegisterForm,
)
from courses.models import CourseModel, CategoryModel

# Create your views here.


class IndexView(generic.View):
    template_name = "courses/index.html"

    def get(self, request):
        courses = CourseModel.objects.order_by("rating")
        categs = CategoryModel.objects.values()
        return render(request, self.template_name, {"courses": courses, "categs": categs})

class CourseView(generic.DetailView):
    template_name = "courses/course.html"
    model = CourseModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryView(generic.DeleteView):
    template_name = "courses/category.html"
    model = CategoryModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = CourseModel.objects.filter(category__id=self.kwargs['pk'])
        return context


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
    template_name = "courses/register.html"
    success_url = reverse_lazy("courses:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("courses:index")


def Logout_View(request):
    logout(request)
    return redirect("courses:index")
