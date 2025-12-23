from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact_us, name="contact"),
    path("404/", views.page_404, name="404"),
    path("500/", views.page_500, name="500")
]
