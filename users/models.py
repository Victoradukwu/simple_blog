from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete='CASCADE')
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username}\'s profile'

	def save(self):
		'''Resizing the image uploaded. This save method overrides the inherited one'''
		super().save()
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

