from django import forms
from django.forms import ModelForm, Textarea
from .models import Project,Profile, Review,Comment
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment']
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
