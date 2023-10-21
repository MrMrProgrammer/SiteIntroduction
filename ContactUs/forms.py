from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Plase include as much detail as possible.'
        })
    )

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
