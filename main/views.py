from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html', {})

def contact_us(request):
    return render(request, 'Contact-Us.html', {})

def about_us(request):
    return render(request, 'About-Us.html', {})

def schedule_appointment(request):
    return render(request, 'Schedule-Appointment.html', {})

def towing_service(request):
    return render(request, 'Towing-Service.html', {})

def student_special(request):
    return render(request, 'Student-Special.html', {})

def business_rates(request):
    return render(request, 'Business-Rates.html', {})

def oil_change_options(request):
    return render(request, 'Oil-Change-Options.html', {})

def payment_options(request):
    return render(request, 'Payment-Options.html', {})

def image_gallery(request):
    return render(request, 'Image-Gallery.html', {})
