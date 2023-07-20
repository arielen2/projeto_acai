from django import forms
from .models import Sorvete

class SorveteForm(forms.ModelForm):
    class Meta:
        model = Sorvete
        fields = '__all__'