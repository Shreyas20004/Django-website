from django import forms
from .models import Location
from localflavor.in_.forms import INZipCodeField


class LocationForm(forms.ModelForm):
    class Meta:
        address1 = forms.CharField(required=True)
        model = Location
        fields = {'address1','address2','city','state'}