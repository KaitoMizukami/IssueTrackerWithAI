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


class IssueCreateForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4'
        }
    ))

    code = forms.CharField(label='Code', widget=forms.Textarea(
        attrs={
            'class': 'input mb-4'
        }
    ))

    description = forms.CharField(label='Note', required=False, widget=forms.Textarea(
        attrs={
            'class': 'input mb-4'
        }
    ))