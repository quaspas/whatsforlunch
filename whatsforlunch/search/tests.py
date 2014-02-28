from django.core.urlresolvers import reverse
from django.test import TestCase
from whatsforlunch.search.connect import api_request
from whatsforlunch.search.form import SearchForm


class SearchConnectTests(TestCase):

    def test_connect_to_api(self):
        url = {
            'term': 'bars',
            'location': 'sf',
            'limit': 1,
        }
        response = api_request(url_params=url)
        self.assertTrue(response)


class SearchFormTests(TestCase):

    def test_search_form_valid(self):
        data = {
            'location': 'toronto',
            'latitude': '',
            'longitude': '',
            'accuracy': '',
            'altitude': '',
            'altitude_accuracy': '',
            'radius': '',
            'term': 'bar',
            'sort': '',
            'category': '',
        }
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_search_form_invalid(self):
        data = {
            'latitude': '',
            'longitude': '',
            'accuracy': '',
            'altitude': '',
            'altitude_accuracy' : '',
            'radius': '',
            'term': '',
            'sort': '',
            'category': '',
        }
        form = SearchForm(data=data)
        self.assertFalse(form.is_valid())


class SearchViewTests(TestCase):

    def test_search_view_get(self):
        response = self.client.get(reverse('search.form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')

    def test_search_view_post_valid(self):
        data = {
            'latitude': 'mylocation',
            'longitude': '',
            'accuracy': '',
            'altitude': '',
            'altitude_accuracy': '',
            'radius': '',
            'term': '',
            'sort': '',
            'category': '',
        }
        response = self.client.post(reverse('search.form'), data=data)
        self.assertEquals(response.status_code, 302)

    def test_search_view_post_invalid(self):
        response = self.client.post(reverse('search.form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')