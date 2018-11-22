import unittest
from app import parcel_app
import json


class TestEndpoints(unittest.TestCase):

	def setUp(self):
		self.app = parcel_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

		self.data = {
			"parcel_id": "1",
			"sender_name": "Harun",
		    "recipient": "Peter",
	    	"destination": "Nakuru",
	        "pickup": "Nairobi",
	        "weight": 2,
	        "username": "arrotech"
	    }

	def test_post(self):
		response = self.client.post(
			'/api/v2/parcels', data=json.dumps(self.data), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result["message"], 'Order created successfully!')
		assert response.status_code == 201

	def test_get(self):
		response = self.client.get(
			'/api/v2/parcels', data=json.dumps(self.data), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
           'success', msg="Not allowed")
		assert response.status_code == 200

	'''def test_get_parcel_by_id(self):
		response = self.client.get(
			'/api/v2/parcels/1', data=json.dumps(self.data), content_type='application/json')
		result = json.loads(response.data.decode())
		assert response.status_code == 200'''

	'''def test_cancel_order(self):
		data = []
		response = self.client.put('/api/v2/parcels/1/cancel',data=json.dumps(data), content_type='application/json')
		result = json.loads(response.data.decode())
		assert response.status_code == 404

	def test_delete_order(self):
		res = self.client.delete(
			"/api/v2/parcels/1/delete", content_type='application/json')
		self.assertEqual(res.status_code, 200)
		self.assertEqual(json.loads(res.data)['message'], "Order deleted")

	def test_no_order_delete(self):
		res = self.client.delete(
			"/api/v2/parcels/1111/delete", content_type='application/json')
		self.assertEqual(res.status_code, 404)
		self.assertEqual(json.loads(res.data)['message'], "Order Unavailable")

	def test_empty_username(self):
		data = {
		"parcel_id": "1",
		"sender_name": "Harun",
		"recipient": "Peter",
		"destination": "Nakuru",
		"pickup": "Nairobi",
		"weight": 2,
		"username": ""
		}

		res = self.client.post("/api/v2/parcels",
			data=json.dumps(data),
			content_type='application/json')
		result = json.loads(res.data.decode())
		assert res.status_code == 400

	def test_invalid_name(self):
		data = {
		"parcel_id": "1",
		"sender_name": "******",
		"recipient": "Peter",
		"destination": "Nakuru",
		"pickup": "Nairobi",
		"weight": 2,
		"username": "arrotech"
		}

		response = self.client.post("/api/v2/parcels", data=json.dumps(data), content_type='application/json')
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_invalid_weight(self):
		data = {
		"parcel_id": "1",
		"sender_name": "George",
		"recipient": "Peter",
		"destination": "Nakuru",
		"pickup": "Nairobi",
		"weight": "2",
		"username": "arrotech"
		}

		response = self.client.post("/api/v2/parcels", data=json.dumps(data), content_type='application/json')
		result = json.loads(response.data.decode())
		assert response.status_code == 400

	def test_key(self):
		data = {
		"parcel_id": "1",
		"sender_name": "George",
		"": "Peter",
		"destination": "Nakuru",
		"pickup": "Nairobi",
		"weight": "2",
		"username": "arrotech"
		}

		response = self.client.post("/api/v2/parcels", data=json.dumps(data), content_type='application/json')
		result = json.loads(response.data.decode())
		assert response.status_code == 400'''







