# coding=utf8


from django import forms
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class SlugFormField(forms.CharField):

    def __init__(self, slugify=None, **kwargs):
        self.slugify = slugify
        super(SlugFormField, self).__init__(**kwargs)

    def validate(self, value):
        print('validate')
        if self.slugify(value) != value:
            raise ValidationError('hievo')


class SlugField(models.CharField):
    description = "Slug (up to %(max_length)s)"

    def __init__(self, *args, **kwargs):
        self.from_field = kwargs.pop('from_field', None)

        self.slugify = kwargs.pop('slugify', slugify)

        kwargs.setdefault('unique', True)
        kwargs.setdefault('db_index', True)
        kwargs.setdefault('max_length', 150)

        super(SlugField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': SlugFormField,
            'slugify': self.slugify,
        }
        defaults.update(kwargs)
        return super(SlugField, self).formfield(**defaults)
