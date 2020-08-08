from django.shortcuts import render

from mainpage.models import Article

# Create your views here.

def index(request):
    my_articles = Article.objects.all()
    return render(request, "index.html", {"articles: my_artcles})