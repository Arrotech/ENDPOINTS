import unittest
import json
from app import parcel_app
from utils.dummy import user_register, user_login 


class TestUsers(unittest.TestCase):

	def setUp(self):
		self.app = parcel_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

		
	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(user_register),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header


	def test_create_account(self):
		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(user_register), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Account created successfully', msg='not allowed')
		assert response.status_code == 201

	def test_signin_account(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'successfully logged in', msg='not allowed')
		assert response.status_code == 200





    