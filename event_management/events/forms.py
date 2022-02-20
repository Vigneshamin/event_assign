from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class EventupdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name","description","maxticket","remticket","event_date","price"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name","description","maxticket","remticket","price"]

