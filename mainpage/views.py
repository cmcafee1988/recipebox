from django.shortcuts import render
from django.http import HttpResponseRedirect

from mainpage.models import Recipe, Author
from mainpage.forms import AddAuthorForm
from mainpage.forms import AddRecipeForm

# Create your views here.

def index(request):
    my_articles = Recipe.objects.all()
    return render(request, "index.html", {"articles": my_articles, "welcome_name": "SE-9"})


def post_detail(request, post_id):
    my_article = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post_id": post_id})



def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data.get('name'),
                bio=data.get('bio')
            )
            return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                author=data.get('author')
            )
            return HttpResponseRedirect('/')

    form = AddRecipeForm()
    return render(request, "add_recipes.html", {"form": form})



