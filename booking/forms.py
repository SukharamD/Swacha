from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    dry_types = forms.MultipleChoiceField(
        required=False,
        choices=[('Plastic', 'Plastic'), ('Paper', 'Paper'), ('Other', 'Other')],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Booking
        fields = ['garbage_type', 'dry_types', 'quantity', 'date', 'time_slot', 'address']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
