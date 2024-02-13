from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Itemlist

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ItemsForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
	class Meta:
		model = Itemlist
		fields = ['SKU','Name','Tags','category','In_stock','Available_stock']