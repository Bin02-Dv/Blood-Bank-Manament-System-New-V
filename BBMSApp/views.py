from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def contact_us(request):
    return render(request, "contactUs.html")

def request_blood(request):
    return render(request, "request-blood.html")


# error handler

def page_404(request, exception):
    return render(request, "404.html")

def page_500(request, exception):
    return render(request, "500.html")


# donor dashboard

def donor_dash(request):
    return render(request, "Donor/dash.html")

def book_appointment(request):
    return render(request, "Donor/book-appointment.html")
