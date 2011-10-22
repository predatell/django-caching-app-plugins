from django.conf import settings
from django.test import TestCase
from django.test.client import Client
import unittest

class ExampleApplication(TestCase):

    #def setUp(self):
    #    pass

    def test_get_homepage(self):
        if settings.DJANGO_SETTINGS_MODULE == 'app_plugins.test_app.settings':
            c = Client()
            response = c.get('/')
            self.assertContains(response, 'site plugin text here')
            self.assertContains(response, 'someapp plugin text here')
        else:
            pass   # test skipped without special settings.py
