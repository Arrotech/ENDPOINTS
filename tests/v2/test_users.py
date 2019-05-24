import json
from utils.dummy import new_register, wrong_register_keys, user_register, user_login, wrong_key_data, wrong_value_data, new_user, login_unexisting_user, invalid_email, username_exists, email_exists
from .base_test import BaseTest

class TestUsers(BaseTest):

	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(user_register),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_register(self):
		response = self.client.post('/api/v2/auth/signup', data=json.dumps(new_register), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Account created successfully', msg='not authorized')
		assert response.status_code == 201

	def test_get_users(self):
		"""Test fetching all offices that have been created."""

		response1 = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_register), content_type='application/json',
			headers=self.get_token())
		response = self.client.get(
			'/api/v2/parcels/users', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_user(self):
		"""Test getting a specific party by id."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_register), content_type='application/json',
			headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/parcels/miriam', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response1.status_code == 200

	def test_get_unexisting_user(self):
		"""Test getting a specific party by id."""

		response1 = self.client.get(
			'/api/v2/parcels/kamau', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'user not found')
		assert response1.status_code == 404

	def test_register_keys(self):
		response = self.client.post('/api/v2/auth/signup', data=json.dumps(wrong_register_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid email key', msg='not authorized')
		assert response.status_code == 400

	def test_existing_email(self):
		response = self.client.post('/api/v2/auth/signup', data=json.dumps(email_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Email Already Exists', msg='not authorized')
		assert response.status_code == 200

	def test_invalid_email(self):
		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(invalid_email), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid Email', msg='not allowed')
		assert response.status_code == 200

	def test_username_exists(self):
		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(username_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Username Already Exists', msg='not allowed')
		assert response.status_code == 200

	def test_signin_account(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'successfully logged in janie', msg='not allowed')
		assert response.status_code == 200

	def test_login_unexisting_user(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(login_unexisting_user), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'user not found', msg='not allowed')
		assert response.status_code == 404
