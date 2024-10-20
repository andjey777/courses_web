from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.Logout_View, name="logout"),
    path("course/<int:pk>/", views.CourseView.as_view(), name="course"),
    path("category/<int:pk>/", views.CategoryView.as_view(), name="categ"),
]
