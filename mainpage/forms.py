from django import forms
from mainpage.models import Author, Recipe
from django.forms import ModelForm


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class EditRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'body']
