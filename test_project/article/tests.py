
from django.test import TestCase, Client


class SlugFieldTestCase(TestCase):

    def test_some(self):
        client = Client()
        response = client.post('/create-article', {
            'name': u'About testing',
            # 'slug': u'bad slug',
            'slug': u'good-slug',
        })
        print('RESPONSE:')
        print(response)
        self.assertEqual(response.status_code, 200)
