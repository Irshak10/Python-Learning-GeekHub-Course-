from django import forms

from .models import Crud


class CrudCreateForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = '__all__'
