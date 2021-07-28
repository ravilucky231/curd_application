from django import forms
from .models import SitiNetwork



class SitiNetworkForm(forms.ModelForm):
    class Meta:
        model = SitiNetwork
        fields="__all__"

