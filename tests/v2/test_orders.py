import json
from utils.dummy import wrong_order_status_key, wrong_order_status_value, correct_order_status, correct_pickup, wrong_pickup_key, wrong_pickup_value, correct_destination, wrong_destination_key_value, wrong_destination_key2, wrong_format_order, wrong_format_destination, wrong_format_sender, wrong_format_pickup, wrong_format_username, wrong_format_recepient, create_order, get_order, user_login, user_register, wrong_key_data, wrong_value_data, wrong_pickup_key, wrong_pickup_value
from .base_test import BaseTest

class TestEndpoints(BaseTest):

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

	def test_get_order(self):
		"""Test getting a specific party by id."""

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json',
			headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/parcels/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response1.status_code == 200

	def test_wrong_sender(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_format_sender), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'sender_name is in wrong format')
		assert response.status_code == 400

	def test_wrong_recipient(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_format_recepient), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'recipient is in wrong format')
		assert response.status_code == 400

	def test_wrong_pickup(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_format_pickup), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'pickup is in wrong format')
		assert response.status_code == 400

	def test_wrong_destination(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_format_destination), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'destination is in wrong format')
		assert response.status_code == 400

	def test_wrong_username(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_format_username), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'username is in wrong format')
		assert response.status_code == 400

	def test_wrong_order(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(wrong_format_order), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Order status is in wrong format')
		assert response.status_code == 400

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
		assert result['status'] == '400'
		assert result['message'] == "resource not found"

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

	def test_destination_correct(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/1', data=json.dumps(correct_destination), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'successfully changed the destination')
		assert response1.status_code == 201

	def test_destination_key(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/1', data=json.dumps(wrong_destination_key2), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'Invalid destination key')
		assert response1.status_code == 400

	def test_destination_key_value(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/1', data=json.dumps(wrong_destination_key_value), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'destination is in wrong format')
		assert response1.status_code == 400

	def test_get_unexisting_parcel(self):
			"""Test getting a specific parcel by id."""

			response1 = self.client.get(
					'/api/v2/parcels/500', content_type='application/json', headers=self.get_token())
			result = json.loads(response1.data.decode())
			self.assertEqual(result['message'],
												'order not found')
			assert response1.status_code == 404

	def test_present_location_correct(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/present-location/1', data=json.dumps(correct_pickup), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'successfully changed the current location')
		assert response1.status_code == 201

	def test_present_location_key(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/present-location/1', data=json.dumps(wrong_pickup_key), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'Invalid pickup key')
		assert response1.status_code == 400

	def test_present_location_key_value(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/present-location/1', data=json.dumps(wrong_pickup_value), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'pickup is in wrong format')
		assert response1.status_code == 400


	def test_order_status_correct(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/order-status/1', data=json.dumps(correct_order_status), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'successfully changed the status')
		assert response1.status_code == 201

	def test_order_status_key(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/order-status/1', data=json.dumps(wrong_order_status_key), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'Invalid order_status key')
		assert response1.status_code == 400

	def test_order_status_key_value(self):

		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(create_order), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parcels/order-status/1', data=json.dumps(wrong_order_status_value), content_type='application/json',
			headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'Order status is in wrong format')
		assert response1.status_code == 400
