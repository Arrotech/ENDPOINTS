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

	

