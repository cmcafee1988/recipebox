from django import forms
from mainpage.models import Author

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)



class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
