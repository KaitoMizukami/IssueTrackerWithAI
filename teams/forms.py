from django import forms

from .models import Team


class TeamCreationForm(forms.ModelForm):
    name = forms.CharField(label='Team Name', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4'
        }
    ))
    auth_code = forms.CharField(label='Authentication Code', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4'
        }
    ))
    class Meta:
        model = Team
        fields = ('name', 'auth_code')


class TeamEnterForm(forms.Form):
    auth_code = forms.CharField(label='Authentication Code', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4'
        }
    ))