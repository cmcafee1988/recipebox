from django.shortcuts import render

from mainpage.models import Recipe
from mainpage.forms import AddAuthorForm

# Create your views here.

def index(request):
    my_articles = Recipe.objects.all()
    return render(request, "index.html", {"articles": my_articles, "welcome_name": "SE-9"})


def post_detail(request, post_id):
    my_article = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post_id": post_id})



def add_author(request):
    if request.method =="POST":
        breakpoint()
        form = AddAuthorForm(request.POST)

    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


