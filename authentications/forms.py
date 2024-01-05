from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', min_length=8)
    confirm_password = forms.CharField(label='confirm password')
    username = forms.CharField(label='username')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('It does not match with password.')
    
    def save(self, commit=False):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'is_staff', 'is_superuser', 'is_active')

    def clean_password(self):
        return self.initial['password']