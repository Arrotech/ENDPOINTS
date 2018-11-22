import unittest
import json
from app import parcel_app


class TestUsers(unittest.TestCase):

	def setUp(self):
		self.app = parcel_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

		self.user = {
	        "email": "arrotechdesign@gmail.com",
	        "password": "20930988",
	        "username": "arrotech",
	        "check_admin": "is admin"
	    }


	def test_create_account(self):
		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(self.user), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Account created successfully', msg='not allowed')
		assert response.status_code == 201

	def test_signin_account(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(self.user), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'successfully logged in', msg='not allowed')
		assert response.status_code == 200

    