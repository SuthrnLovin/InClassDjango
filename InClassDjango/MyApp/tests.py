"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from .models import Unit
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.





class UnitTest(TestCase):

    def test_english_exists(self):

        Unit.objects.create(Title='English')

        field_object = Unit.objects.filter(Title='English')

        if field_object.exists():
            print("SUCCESS: English unit exists")
        else:
            print("FAILED")