"""mechanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('about-us', views.about_us, name='about-us'),
    # path('schedule-appointment', views.schedule_appointment, name='schedule-appointment'),
    path('towing-service', views.towing_service, name='towing-service'),
    path('student-special', views.student_special, name='student-special'),
    path('business-rates', views.business_rates, name='business-rates'),
    path('oil-change-options', views.oil_change_options, name='oil-change-options'),
    path('payment-options', views.payment_options, name='payment-options'),
    path('image-gallery', views.image_gallery, name='image-gallery'),
]
