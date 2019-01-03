'''A module of tests for blog views'''
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
from users.models import Profile

class TestUserViews(TestCase):
	'''Test class for user views'''

	def setUp(self):
		self.client = Client()
		# self.auth_user = mommy.make('User')
		# self.client.force_login(self.auth_user)

	def test_register_view(self):
		test_user = mommy.prepare('User', email='abc@abc.com')

		resp = self.client.post(reverse('register'), {'username': test_user.username, 'password1': test_user.password, 'password2': test_user.password, 'email': test_user.email})

		self.assertEqual(resp.status_code, 302)
		self.assertNotEqual(User.objects.get(username=test_user.username), None)
		self.assertNotEqual(Profile.objects.all().filter(user__email=test_user.email), None) # assert that the user profile is automatically created
