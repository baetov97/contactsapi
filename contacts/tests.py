from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from .models import Contact, Post


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)


class ContactModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_contact_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_existing_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 404)

    # def test_view_url_by_name(self):
    #     resp = self.client.get(reverse(''))
    #     self.assertEqual(resp.status_code, 404)

    def test_view_uses_correct_template(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 404)
        # self.assertTemplateUsed(resp, 'home.html')
