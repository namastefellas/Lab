from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model



class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField( strip=False, required=True, widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput, strip=False, label='Password Confirmation')
    email = forms.CharField(required=True, label='Email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords dont match')
        if not first_name and not last_name:
            raise forms.ValidationError('Fill one of the fields: First Name or Last Name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']