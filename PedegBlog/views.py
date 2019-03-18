from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article
# Create your views here.
def articalindex(request):
    latest_article_list = Article.objects.order_by('-article_time')[:5]
    template = loader.get_template('PedegBlog/articalIndex.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))

def articalcontain(request,id):
    return HttpResponse("You're looking at question %s." % id)

