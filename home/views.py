from django.shortcuts import render,redirect
from . models import Booking
from django.contrib import messages

# Create your views here.
def Homepage(request):
    return render(request, 'index.html')

def check(request):
    return render(request, 'heartform.html')


def Bookings(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Booking.objects.create(
            name=name,
            age=age,
            phone=phone,
            category=category,
            email=email,
            message = message,
        )
        messages.success(request, f"Thank you {name}, your appointment request has been received!")

        # Add a success message
        return redirect('booking')

    # Render the default form for booking
    return render(request, 'Appointment.html')
