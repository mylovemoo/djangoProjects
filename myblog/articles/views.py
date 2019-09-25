from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import article

# Create your views here.
def index(request):
    latest_article_list = article.objects.order_by('-article_date')[:5]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_id):
    try:
        art = article.objects.get(pk=article_id)
    except article.DoesNotExist:
        raise Http404("article does not exist")
    return render(request, 'articles/detail.html', {'art':art})

def menu(request):
    response = "You're looking at the menu."
    return HttpResponse(response)

