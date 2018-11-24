import unittest
from app import parcel_app
import json
from utils.dummy import create_order, get_order, user_login, user_register, wrong_key_data, wrong_value_data, wrong_pickup_key, wrong_pickup_value, wrong_destination_key, wrong_destination_value


class TestEndpoints(unittest.TestCase):

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

	def test_create_order(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Order created successfully!')
		assert response.status_code == 201

	def test_get_one_order(self):
		response = self.client.get(
			'/api/v2/parcels/1', data=json.dumps(get_order), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
           'success', msg="Not allowed")
		assert response.status_code == 200

	def test_all_orders(self):
		response = self.client.get(
			'/api/v2/parcels', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 200

	def test_wrong_url(self):
		response = self.client.get(
			'/api/v2/parce', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_wrong_key(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_key_data), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_wrong_value(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_value_data), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_wrong_pickup_key(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_pickup_key), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_wrong_pickup_key(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_pickup_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_wrong_destination_key(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_destination_key), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_wrong_destination_value(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_destination_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	




