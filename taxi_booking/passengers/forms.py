from django import forms
from .models import Passenger,Booking

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Passenger
        fields = ['username', 'phone_number', 'date_of_birth', 'password']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    passenger_id = forms.IntegerField()
    pick_up_location = forms.CharField(max_length=100)
    destination= forms.CharField(max_length=100)
    number_of_passengers = forms.IntegerField()
    date = forms.DateField()
    time = forms.TimeField()
     
    class Meta:
        model = Booking
        fields = ['pick_up_location', 'destination', 'number_of_passengers', 'date', 'time'] 