from django import forms
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import *


class Booking(forms.ModelForm):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'John Smith'}))
	phone = PhoneNumberField()
	persons = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': '1-20'}))
	date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))

	class Meta:
		model = Reservation
		fields = '__all__'

class AddForm(forms.ModelForm):
	class Meta:
		model = Food
		fields = '__all__'

class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = '__all__'
