
from django.db import models

from slugfield.slugfield import SlugField


class Article(models.Model):
    name = models.CharField(max_length=100)
    # slug = SlugField(slugify=lambda x: 'hui')
    slug = SlugField()
