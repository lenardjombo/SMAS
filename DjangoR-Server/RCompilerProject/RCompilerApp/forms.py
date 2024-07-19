from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    admission_number = forms.CharField(max_length=20, required=True, label="Admission Number")

    class Meta:
        model = User
        fields = ('admission_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['admission_number']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    admission_number = forms.CharField(max_length=20, required=True, label="Admission Number")

    def confirm_login_allowed(self, user):
        if user.username != self.cleaned_data['admission_number']:
            raise forms.ValidationError("Invalid admission number or password.")
