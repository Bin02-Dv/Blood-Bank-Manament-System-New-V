from django.shortcuts import render

# Create your views here.


# admin

def admin_dash(request):
    return render(request, "dash/admin-dash/dash.html")

# donor

def donor_dash(request):
    return render(request, "donor/dash.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")
