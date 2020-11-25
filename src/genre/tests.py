from django.test import TestCase
import unittest
from .models import Genre
from django.urls import reverse_lazy, reverse
#from unittest import mock

# Create your tests here.
class TestGenre(unittest.TestCase):
    def setUp(self):
        Genre.objects.create(name='lion2')

    def test_create_obj_has_pub_data(self):
        post = Genre.objects.get(name='lion')
        self.assertIsNotNone(post.name)


class ViewTest(TestCase):
    def test_genre(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])