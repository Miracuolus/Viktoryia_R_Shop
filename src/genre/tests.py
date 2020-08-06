from django.test import TestCase
import unittest
from .models import Genre
#from unittest import mock

# Create your tests here.
class TestBook(unittest.TestCase):
    def setUp(self):
        Genre.objects.create(name='lion')

    def test_create_obj_has_pub_data(self):
        post = Genre.objects.get(name='lion')
        self.assertIsNotNone(post.name)