from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from mainpage.models import Recipe, Author
from mainpage.forms import AddAuthorForm
from mainpage.forms import AddRecipeForm, LoginForm, SignupForm


# Create your views here.

def index(request):
    my_articles = Recipe.objects.all()
    return render(request, "index.html", {"articles": my_articles, "welcome_name": "SE-9"})


def post_detail(request, post_id):
    my_article = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_article})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(
                name=data.get('name'),
                bio=data.get('bio')
            )
            return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


@staff_member_required
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



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("mainpage")))

    form = LoginForm()
    return render(request, "add_recipes.html", {"form": form})



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("mainpage"))

    form = SignupForm()
    return render(request, "add_recipes.html", {"form": form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



