from django import forms


class contactForm(forms.Form):
    name = forms.CharField(max_length=300,)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True,widget=forms.Textarea)