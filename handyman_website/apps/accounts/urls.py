from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="accounts"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),
    # Django auth
    path(
        "login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout", 
         auth_views.LogoutView.as_view(template_name="accounts/logout"), 
         name="logout"),
]