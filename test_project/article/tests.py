from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from slugfield.main import SlugFormField


class SlugFieldTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_valid(self):
        response = self.client.post('/create-article', {
            'name': u'Bad slug',
            'slug': u'bad slug',
        })
        self.assertEqual(response.status_code, 200)

    def test_form_field(self):
        self.assertFieldOutput(SlugFormField,
            valid={'valid-slug': 'valid-slug'},
            invalid={'invalid slug': [u'Invalid']},
        )
