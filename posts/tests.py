from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):

	def setUp(self):
		Post.objects.create(text="This is a sample")

	def test_text_content(self):
		post=Post.objects.get(id=1)
		expected= f'{post.text}'
		self.assertEqual(expected,"This is a sample")

class HomePageTestView(TestCase):

	def setUp(self):
		Post.objects.create(text="The second text piece")

	def test_view_url_exists(self):
		resp=self.client.get('/')
		self.assertEqual(resp.status_code,200)

	def test_view_url_by_name(self):
		resp=self.client.get(reverse('home'))
		self.assertEqual(resp.status_code,200)

	def test_view_uses_correct_template(self):
		resp=self.client.get(reverse('home'))
		self.assertEqual(resp.status_code,200)
		self.assertTemplateUsed(resp,'home.html')

