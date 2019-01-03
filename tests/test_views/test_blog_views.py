'''A module of tests for blog views'''
import json
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post

class TestBlogViews(TestCase):
	'''Test class for blog views'''

	def setUp(self):
		self.client = Client()
		self.auth_user = mommy.make('User')
		self.client.force_login(self.auth_user)

	def test_about_view(self):
		resp = self.client.get(reverse('blog-about'))

		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'blog/about.html')

	def test_post_list_view(self):
		mommy.make('Post', author=self.auth_user, _quantity=8)

		resp = self.client.get(reverse('blog-home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'blog/home.html')
		self.assertContains(resp, self.auth_user.username)

	def test_post_detail_view(self):
		blog = mommy.make('Post')

		resp = self.client.get(reverse('post-detail', args=[blog.id]))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'blog/post_detail.html')
		self.assertContains(resp, blog.content)

	def test_post_create_view(self):
		blog = mommy.prepare('Post')
		data = {'title': blog.title, 'content': blog.content}

		resp = self.client.post(reverse('blog-create'), data)
		self.assertEqual(resp.status_code, 302)
		self.assertEqual(Post.objects.first().title, blog.title)

	def test_post_delete_view(self):
		blog = mommy.make('Post', author=self.auth_user)

		resp = self.client.delete(reverse('post-delete', args=[blog.id]))
		self.assertEqual(resp.status_code, 302)
		self.assertEqual(Post.objects.all().count(), 0)

	def test_post_update_view(self):
		blog = mommy.make('Post', author=self.auth_user)

		resp = self.client.post(reverse('post-update', args=[blog.id]), {'title': blog.title, 'content': 'new content'})
		self.assertEqual(resp.status_code, 302)
		self.assertEqual(Post.objects.all().count(), 1)
		self.assertEqual(Post.objects.first().title, blog.title)
		self.assertEqual(Post.objects.first().content, 'new content')

	def test_user_posts_view(self):
		mommy.make('Post', author=self.auth_user, _quantity=3)
		mommy.make('Post', _quantity=2)

		resp = self.client.get(reverse('user-posts', args=[self.auth_user.username]))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'blog/user_posts.html')
		self.assertContains(resp, self.auth_user.username)
		self.assertEqual(resp.context['posts'].count(), 3)
