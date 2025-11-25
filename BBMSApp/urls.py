from django.urls import path

from . import views

urlpatterns = [
    # admin
    path("admin/dash/", views.admin_dash, name="admin_dash"),
    
    # donor
    path("donor/dash/", views.donor_dash, name="donor-dash"),
    
    # auth
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register")
]
