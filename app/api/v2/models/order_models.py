from app.api.v2.models.database import Database
import json
from flask_jwt_extended import jwt_required

Database().create_table()

class OrdersModel(Database):
	"""Initiallization."""

	def __init__(self,sender_name=None,recipient=None,destination=None,pickup=None,weight=None,username=None, order_status="Pending"):
		super().__init__()
		self.sender_name = sender_name
		self.recipient = recipient
		self.destination = destination
		self.pickup = pickup
		self.weight = weight
		self.username = username
		self.order_status = order_status

	def save(self, sender_name, recipient, destination, pickup, weight, username, order_status):
		"""Create a new orders."""

		print(sender_name, recipient, destination, pickup, weight, username)
		self.curr.execute(
			''' INSERT INTO orders(sender_name,recipient,destination,pickup,weight,username,order_status)\
			VALUES('{}','{}','{}','{}','{}','{}','{}')\
			 RETURNING sender_name, recipient, destination, pickup, weight, username, order_status'''\
			.format(sender_name, recipient, destination, pickup, weight, username, order_status))
		orders = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return orders

	def get_all_parcels(self):
		"""Fetch all orders"""

		self.curr.execute(''' SELECT * FROM orders''')
		orders = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()
		return json.dumps(orders, default=str)

	def get_parcel_by_id(self, parcel_id):
		"""Fetch a single order"""

		self.curr.execute(""" SELECT * FROM orders WHERE parcel_id={}""".format(parcel_id ))
		order = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(order, default=str)

	def change_destination(self, parcel_id, destination):
		"""User can Change destination."""

		self.curr.execute("""UPDATE orders\
			SET destination='{}'\
			WHERE parcel_id={} RETURNING destination, pickup"""\
			.format(parcel_id,destination))
		orders = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return orders

	def change_present_location(self, parcel_id, pickup):
		"""Admin can Change present location"""

		self.curr.execute("""UPDATE orders\
			SET pickup='{}'\
			WHERE parcel_id={} RETURNING pickup, parcel_id"""\
			.format(parcel_id,pickup))
		orders = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return orders

	def change_status(self, parcel_id, order_status):
		"""Change order status"""

		self.curr.execute("""UPDATE orders\
			SET order_status='{}'\
			WHERE parcel_id={} RETURNING order_status, parcel_id"""\
			.format(parcel_id,order_status))
		orders = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return orders
