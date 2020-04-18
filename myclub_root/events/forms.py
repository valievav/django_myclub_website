from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    required_css_class = 'required'   # will be used to add asterisk to required fields

    class Meta:
        model = Venue
        fields = '__all__'

    def clean(self):
        """
        Validates phone and email
        """
        cleaned_data = super().clean()  # validates data
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email_address")
        if not (phone or email):
            raise forms.ValidationError("You must enter a phone number or an email, or both")
