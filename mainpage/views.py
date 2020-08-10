from django.shortcuts import render

from mainpage.models import Article

# Create your views here.

def index(request):
    my_articles = Article.objects.all()
    return render(request, "index.html", {"articles": my_articles, "welcome_name": "SE-9"})


def post_detail(request, post_id):
    my_article = Article.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post_id": post_id})