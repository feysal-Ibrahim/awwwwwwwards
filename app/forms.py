from django import forms
from .models import Project,Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields='__all__'
