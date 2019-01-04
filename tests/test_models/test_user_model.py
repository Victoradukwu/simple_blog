from django.test import TestCase, Client
from users.models import Profile
from model_mommy import mommy


class TestProfileModel(TestCase):

	def test_can_create_profile(self):
		profile = mommy.prepare('Profile', user=mommy.make('User'))

		self.assertEqual(Profile.objects.all().count(), 1)
		self.assertIsInstance(Profile.objects.get(pk=1), Profile)
		self.assertEqual(Profile.objects.get(pk=1).image, profile.image)

	def test_can_update_posts(self):
		mommy.prepare('Profile', user=mommy.make('User', email='abc@abc.com'))

		profile = Profile.objects.first()
		profile.user.email = 'new@imail.com'
		profile.user.save()

		self.assertEqual(Profile.objects.get(pk=1).user.email, 'new@imail.com')

	def test_can_delete_profile(self):
		mommy.prepare('Profile', user=mommy.make('User', email='abc@abc.com'))

		profile = Profile.objects.first()
		profile.delete()

		with self.assertRaises(Profile.DoesNotExist):
			Profile.objects.get(image=profile.image)
