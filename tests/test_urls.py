'''Test module for all urls'''
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import (
	LoginView,
	LogoutView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView)
from blog.views import (
	about,
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView)
from users.views import register, user_profile


class TestUrls(SimpleTestCase):
	'''Test class for testing url resolutions'''

	def test_register_url_resolves(self):
		'''Testing the register url'''
		url = reverse('register')

		self.assertEqual(resolve(url).func, register)
		self.assertEqual(resolve(url).url_name, 'register')

	def test_profile_url_resolves(self):
		'''Testing the profile url'''
		url = reverse('profile')

		self.assertEqual(resolve(url).func, user_profile)
		self.assertEqual(resolve(url).url_name, 'profile')

	def test_login_url_resolves(self):
		'''Testing the login url'''
		url = reverse('login')

		self.assertEqual(resolve(url).func.view_class, LoginView)
		self.assertEqual(resolve(url).url_name, 'login')

	def test_logout_url_resolves(self):
		'''Testing the logout url'''
		url = reverse('logout')

		self.assertEqual(resolve(url).func.view_class, LogoutView)
		self.assertEqual(resolve(url).url_name, 'logout')

	def test_password_reset_url_resolves(self):
		'''Testing the password reset url'''
		url = reverse('password_reset')

		self.assertEqual(resolve(url).func.view_class, PasswordResetView)
		self.assertEqual(resolve(url).url_name, 'password_reset')

	def test_password_reset_confirm_url_resolves(self):
		'''Testing the password reset Confirm url'''
		url = reverse('password_reset_confirm', kwargs={'uidb64': 'bvnqebmhbwejh', 'token': 'wjjktgn3kjgkl3jglk'})

		self.assertEqual(resolve(url).func.view_class, PasswordResetConfirmView)
		self.assertEqual(resolve(url).url_name, 'password_reset_confirm')

	def test_password_reset_done_url_resolves(self):
		'''Testing the password_reset_done url'''
		url = reverse('password_reset_done')

		self.assertEqual(resolve(url).func.view_class, PasswordResetDoneView)
		self.assertEqual(resolve(url).url_name, 'password_reset_done')

	def test_password_reset_complete_url_resolves(self):
		'''Testing the password_reset_complete url'''
		url = reverse('password_reset_complete')

		self.assertEqual(resolve(url).func.view_class, PasswordResetCompleteView)
		self.assertEqual(resolve(url).url_name, 'password_reset_complete')

	def test_home_url_resolves(self):
		'''Testing the home url'''
		url = reverse('blog-home')

		self.assertEqual(resolve(url).func.view_class, PostListView)
		self.assertEqual(resolve(url).url_name, 'blog-home')

	def test_about_url_resolves(self):
		'''Testing the about url'''
		url = reverse('blog-about')

		self.assertEqual(resolve(url).func, about)
		self.assertEqual(resolve(url).url_name, 'blog-about')

	def test_user_posts_url_resolves(self):
		'''Testing the user-posts'''
		url = reverse('user-posts', kwargs={'username': 'bvnqebmhbwejh'})

		self.assertEqual(resolve(url).func.view_class, UserPostListView)
		self.assertEqual(resolve(url).url_name, 'user-posts')

	def test_blog_create_url_resolves(self):
		'''Testing the blog-create'''
		url = reverse('blog-create')

		self.assertEqual(resolve(url).func.view_class, PostCreateView)
		self.assertEqual(resolve(url).url_name, 'blog-create')

	def test_post_detail_url_resolves(self):
		'''Testing the post-detail'''
		url = reverse('post-detail', kwargs={'pk': 1})

		self.assertEqual(resolve(url).func.view_class, PostDetailView)
		self.assertEqual(resolve(url).url_name, 'post-detail')

	def test_post_delete_url_resolves(self):
		'''Testing the post-delete'''
		url = reverse('post-delete', kwargs={'pk': 1})

		self.assertEqual(resolve(url).func.view_class, PostDeleteView)
		self.assertEqual(resolve(url).url_name, 'post-delete')

	def test_post_update_url_resolves(self):
		'''Testing the post-update'''
		url = reverse('post-update', kwargs={'pk': 1})

		self.assertEqual(resolve(url).func.view_class, PostUpdateView)
		self.assertEqual(resolve(url).url_name, 'post-update')
