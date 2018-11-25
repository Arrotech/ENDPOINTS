import unittest
import json
from app import parcel_app
from utils.dummy import user_register, user_login, wrong_key_data, wrong_value_data


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


	def test_username_exists(self):
		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(user_register), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Username Already Exists', msg='not allowed')
		assert response.status_code == 200

	def test_signin_account(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'successfully logged in', msg='not allowed')
		assert response.status_code == 200


	

	def test_invalid_name(self):

		res = self.client.post(
			"/api/v2/parcels",
			data=json.dumps(wrong_key_data), content_type="application/json", headers=self.get_token())

		self.assertEqual(res.status_code, 400)
		self.assertEqual(
			json.loads(res.data)['message'], "Invalid sender_name key")

	def test_invalid_username(self):
		

		res = self.client.post(
			"/api/v2/parcels",
			data=json.dumps(wrong_value_data), content_type="application/json", headers=self.get_token())

		self.assertEqual(res.status_code, 400)
		self.assertEqual(
			json.loads(res.data)['message'], "pickup is in wrong format")

	def test_unexisting_order(self):

		res = self.client.get(
			"/api/v2/parcels/568", content_type="application/json", headers=self.get_token())
		self.assertEqual(res.status_code, 404)
		self.assertEqual(json.loads(res.data)['message'], "Order Not Found")

	def test_invalid_destination(self):

		res = self.client.post(
			"/api/v2/parcels",
			data=json.dumps(wrong_value_data), content_type="application/json", headers=self.get_token())

		self.assertEqual(res.status_code, 400)
		self.assertEqual(
			json.loads(res.data)['message'],
			"pickup is in wrong format")

	



    