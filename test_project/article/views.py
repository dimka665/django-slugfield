
from django.forms import ModelForm
from django.http import HttpResponse

from article.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article


def create_article(request):
    article_form = ArticleForm(request.POST)

    if article_form.is_valid():
        response = HttpResponse('valid')
    else:
        response = HttpResponse('invalid')

    return response
