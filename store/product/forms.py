from django import forms
from .models import Booking

class Dateinput(forms.DateInput):
    input_type= 'date'

class BookingForm(forms.ModelForm): #Always try to give form class name as 'classnameForms' format
    class Meta:
        model = Booking
        fields = '__all__'  # '__all__' is used when all the fields of booking class is needed to be imported, if a specific class only needed give the name of that particular field in the form of a list like [p_name, p_phone]

        widgets = {            # widgets are used to add additional features, here the date format with calender will appear in date field
            'booking_date': Dateinput(),
        }
        
        labels = {
            'p_name' : "Patient Name:",
            'p_phone' : "Patient Phone:",
            'p_email' : "Patient Email:",
            'booking_date' : "Booking Date:",
        }

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')

