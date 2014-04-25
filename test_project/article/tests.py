
from django.test import TestCase, Client


class SlugFieldTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_valid_slug(self):
        response = self.client.post('/create-article', {
            'name': u'About testing',
            'slug': u'valid-slug',
        })
        self.assertNotContains(response, 'class="errorlist"')
        self.assertContains(response, 'value="valid-slug"')

    def test_invalid_slug(self):
        response = self.client.post('/create-article', {
            'name': u'About testing',
            'slug': u'invalid    slug',
        })
        self.assertContains(response, 'class="errorlist"')
        self.assertContains(response, 'value="invalid    slug"')

    def test_empty_slug(self):
        response = self.client.post('/create-article', {
            'name': u'About testing',
            'slug': u'',
        })
        self.assertContains(response, 'class="errorlist"')
        self.assertContains(response, 'value="about-testing?"')
