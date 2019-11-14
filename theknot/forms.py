from django import forms

from .models import *
class GuestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.fields['attending_wedding'].label = "Wedding"
        self.fields['attending_reception'].label = "Reception"

    attending_wedding  = forms.ChoiceField(
        choices=[(1, 'Yes, I will be there!'), (0, "I wish I could. ")],
        widget=forms.RadioSelect
    )
    attending_reception  = forms.ChoiceField(
        choices=[(1, 'Yes, I will be there!'), (0, "I wish I could. ")],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Guest
        fields = ("first_name" , "last_name" , "email" , "attending_wedding" , "attending_reception" , "additional_guests", "message" )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input_field'}),
            'last_name': forms.TextInput(attrs={'class': 'input_field'}),
            'email': forms.TextInput(attrs={'class': 'input_field'}),
            'message': forms.Textarea(attrs={'cols': 30, 'rows': 4}),

        }

