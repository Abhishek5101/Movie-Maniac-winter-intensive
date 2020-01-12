from unittest import TestCase, main as unittest_main
from flaskblog import app


class ProjectTests(TestCase):
	"""Flask tests."""

	def setUp(self):
		"""Stuff to do before every test."""

		# Get the Flask test client
		self.client = app.test_client()

		# Show Flask errors that happen during tests
		app.config['TESTING'] = True

	def test_index(self):
		"""Test the project homepage."""
		result = self.client.get('/')
		self.assertEqual(result.status, '200 OK')

	def test_register(self):
		"""Test the project cartpage."""
		result = self.client.get('/register')
		self.assertEqual(result.status, '200 OK')
	
	def test_login(self):
		"""Test for Login Route"""
		result = self.client.get('/login')
		self.assertEqual(result.status, '200 OK')
	
	def test_movies(self):
		"""Test for movies Route"""
		result = self.client.get('/movies')
		self.assertEqual(result.status, '200 OK')


if __name__ == '__main__':
	unittest_main()