from django import forms

from .models import Birthday


class BirthdayForm(forms.Form):
    
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
        fields = '__all__'
