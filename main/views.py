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
