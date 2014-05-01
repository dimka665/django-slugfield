=======================================
django-slugfield
=======================================

Install
===================

pip install django-slugfield

Usage
===================

.. code-block:: python

    from django import forms
    from slugfield import SlugFormField
    
    class ArticleForm(forms.Form):
        name = forms.CharField(max_length=100)
        slug = SlugFormField(populate_from='name')
