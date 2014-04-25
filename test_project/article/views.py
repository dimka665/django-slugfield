
from django.forms import ModelForm
from django.http import HttpResponse

from article.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article


def create_article(request):
    article_form = ArticleForm(request.POST)

    # if article_form.is_valid():
    #     pass
    # else:
    #     response = HttpResponse('invalid')
    #

    # print('str(form)')
    string = str(article_form)
    # print('string: ')
    print(string)
    print('')
    return HttpResponse(string + '\n\n')
    # return HttpResponse(article_form)
