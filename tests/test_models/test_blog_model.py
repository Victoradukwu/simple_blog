from django.test import TestCase, Client
from blog.models import Post
from model_mommy import mommy


class TestBlogModel(TestCase):
	
	def test_can_create_post(self):
		blog = mommy.prepare('Post', author=mommy.make('User'))
		Post.objects.create(title=blog.title, content=blog.content, author=blog.author)

		self.assertEqual(Post.objects.all().count(), 1)
		self.assertIsInstance(Post.objects.get(pk=1), Post)
		self.assertEqual(Post.objects.get(pk=1).title, blog.title)

	def test_can_retrieve_posts(self):
		mommy.make('Post', author=mommy.make('User'), _quantity=10)

		posts = Post.objects.all()

		self.assertEqual(posts.count(), 10)

	def test_can_update_posts(self):
		blog = mommy.make('Post', author=mommy.make('User'))

		post = Post.objects.first()
		post.title='New title'
		post.save()

		self.assertEqual(Post.objects.get(pk=1).title, 'New title')

	def test_can_delete_posts(self):
		blog = mommy.make('Post', author=mommy.make('User'))

		post = Post.objects.first()
		post.delete()

		with self.assertRaises(Post.DoesNotExist):
			Post.objects.get(title=blog.title)

	def test_get_absolute_url(self):
		blog = mommy.make('Post', author=mommy.make('User'))

		post = Post.objects.first()

		self.assertEqual(post.get_absolute_url(), f'/post/{post.id}/')
