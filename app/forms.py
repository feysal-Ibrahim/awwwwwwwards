from django import forms
from .models import Project,Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields='__all__'
