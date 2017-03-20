from django.test import TestCase
from django.urls import resolve
from kanq_app.views.home import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)