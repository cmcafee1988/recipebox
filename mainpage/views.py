from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from mainpage.models import Recipe, Author
from mainpage.forms import AddAuthorForm
from mainpage.forms import AddRecipeForm, LoginForm, SignupForm, EditRecipeForm


# Create your views here.

def index(request):
    my_articles = Recipe.objects.all()
    return render(request, "index.html", {"articles": my_articles, "welcome_name": "SE-9"})


def post_detail(request, post_id):
    my_article = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_article})


def author_details(request, author_id):
    authors_recipes = Recipe.objects.filter(
        author=Author.objects.get(id=author_id))
    this_author = Author.objects.filter(id=author_id).first()
    return render(request, 'author_detail.html', {'author': this_author, "recipes": authors_recipes})


def author_favorites(request, author_id):
    favorite_recipes = Author.objects.get(id=author_id).favorites.all()
    this_author = Author.objects.filter(id=author_id).first()
    return render(request, 'author_favorites.html', {'author': this_author, "recipes": favorite_recipes})


@staff_member_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Author.objects.create(
                name=data.get('name'),
                bio=data.get('bio'),
                new_user=User.objects.create_user(username=data.get(
                    "username"), password=data.get("password"))
            )
            return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                author=request.user.author
            )
            return HttpResponseRedirect('/')

    form = AddRecipeForm()
    return render(request, "add_recipes.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
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
            new_user = User.objects.create_user(username=data.get(
                "username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("mainpage"))

    form = SignupForm()
    return render(request, "add_recipes.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def edit_view(request, post_id):
    post = Recipe.objects.get(id=post_id)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('mainpage'))
    form = EditRecipeForm(instance=post)
    if request.user.is_staff:
        return render(request, 'add_recipes.html', {'form': form})
    if request.user.author == post.author:
        return render(request, 'add_recipes.html', {'form': form})
    return HttpResponseRedirect(reverse('mainpage'))


@login_required
def favorite_view(request, post_id):
    request.user.author.favorites.add(post_id)
    return HttpResponseRedirect(reverse("mainpage"))
