from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from .models import Passenger, Booking
from .forms import LoginForm,BookingForm
# Create your views here.
def home(request):
    return render(request, 'passengers/home.html')

def about(request):
    return render(request, 'passengers/about.html')

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after sign-up
    else:
        form = SignUpForm()
    return render(request, 'passengers/sign_up.html', {'form': form})


def passenger_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                passenger = Passenger.objects.get(username=username, password=password)
                request.session['passenger_id'] = passenger.id  # Store session
                return redirect('passenger_dashboard')  # Redirect to student dashboard
            except Passenger.DoesNotExist:
                error_message = "Invalid username or password."

    else:
        form = LoginForm()
        error_message = None

    return render(request, 'passengers/login.html', {'form': form, 'error_message': error_message})


def passenger_dashboard(response):

    if response.method == "POST":
        form = BookingForm(response.POST)
        if form.is_valid():
            pick_up_location = form.cleaned_data['pick_up_location']
            destination = form.cleaned_data['destination']
            number_of_passengers = form.cleaned_data['number_of_passengers']
            booking_date = form.cleaned_data['date']
            booking_time = form.cleaned_data['time']
            passenger = Passenger.objects.get(id=response.session['passenger_id'])
            booking = user.booking_set.create(
                pick_up_location=pick_up_location, 
                destination=destination, 
                number_of_passengers=number_of_passengers, 
                date=booking_date, 
                time=booking_time
            )
            booking.save()
            return redirect('passenger_success')  
    else:
        form = BookingForm()

    return render(response, 'passengers/details.html', { 'form': form})

def passenger_success(request):
    
    if 'passenger_id' not in request.session:
        return redirect('passenger_login')  # Redirect to login if not logged in

    passenger = Passenger.objects.get(id=request.session['passenger_id'])
    return render(request, 'passengers/success.html', {'passenger': passenger})


