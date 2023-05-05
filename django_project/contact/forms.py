from django import forms

from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

"""         widgets = {
            'name': forms.TextInput(),
            'email': forms.TextInput(),
            'website': forms.TextInput(),
            'message': forms.TextInput()
        } """