# coding=utf8

import re

from django import forms
from django.db import models
from django.forms.widgets import TextInput
from django.utils.text import slugify as django_slugify
from django.core.exceptions import ValidationError


class SlugFormField(forms.CharField):

    def __init__(self, slugify=django_slugify, populate_from=None, **kwargs):
        self.slugify = slugify

        widget = kwargs.get('widget', TextInput)

        widget_is_class = isinstance(widget, type)
        if widget_is_class:
            widget = widget()

        widget_class = widget.__class__
        def value_from_datadict(data, files, name):
            value = super(widget_class, widget_self).value_from_datadict(data, files, name)
            # value = data.get(name)
            if value:
                return value
            elif populate_from:
                # some magic
                html_name_re = re.compile('({})$'.format(re.escape(name)))
                name = html_name_re.sub(populate_from, name)
                value = self.slugify(data.get(name, ''))
                if value:
                    value += '?'
                return value

        widget.value_from_datadict = value_from_datadict
        kwargs['widget'] = widget

        super(SlugFormField, self).__init__(**kwargs)

    def validate(self, value):
        if self.slugify(value) != value:
            raise ValidationError('Invalid')
        super(SlugFormField, self).validate(value)


class SlugField(models.CharField):
    description = 'Slug (up to %(max_length)s)'
    default_error_message = "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens."

    def __init__(self, *args, **kwargs):

        self.populate_from = kwargs.pop('populate_from', None)
        self.slugify = kwargs.pop('slugify', django_slugify)
        self.empty_values = (None,)

        self.invalid_slug_message = kwargs.pop('mes', 'invalid slug mes')

        kwargs.setdefault('unique', True)
        kwargs.setdefault('db_index', True)
        kwargs.setdefault('max_length', 200)

        super(SlugField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': SlugFormField,
            'slugify': self.slugify,
            'populate_from': self.populate_from,
            # 'widget': TextInput,
            'widget': TextInput(attrs={'size': '40'}),
        }
        defaults.update(kwargs)
        return super(SlugField, self).formfield(**defaults)
