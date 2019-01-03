'''Module of tests for forms of users app'''
from django.test import TestCase
from model_mommy import mommy
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class TestUserForms(TestCase):
	'''Module of tests for forms of users app'''

	def test_user_register_form_validate(self):
		user = mommy.prepare('User', email='user@user.com')
		form = UserRegisterForm(data={
			'email': user.email,
			'username': user.username,
			'password1': user.password,
			'password2': user.password
			})

		self.assertTrue(form.is_valid())

	def test_user_register_form_invalid(self):
		form = UserRegisterForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEqual(len(form.errors), 4)

	def test_user_update_form_validate(self):
		user = mommy.prepare('User', email='user@user.com')
		form = UserUpdateForm(data={'email': user.email, 'username': user.username})

		self.assertTrue(form.is_valid())	

	def test_profile_update_form_validate(self):
		profile = mommy.prepare('Profile')
		form = ProfileUpdateForm(data={'image': profile.image})

		self.assertTrue(form.is_valid())
