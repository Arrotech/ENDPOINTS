from app.api.v2.models.database import Database
import json

class OrdersModel(Database):


	def __init__(self,sender_name=None,recipient=None,destination=None,pickup=None,weight=None,username=None):
		super().__init__()
		self.sender_name = sender_name
		self.recipient = recipient
		self.destination = destination
		self.pickup = pickup
		self.weight = weight
		self.username = username


	def save(self, sender_name, recipient, destination, pickup, weight, username):
		print(sender_name, recipient, destination, pickup, weight, username)

		self.curr.execute(
			''' INSERT INTO orders(sender_name,recipient,destination,pickup,weight,username)\
			VALUES('{}','{}','{}','{}','{}','{}') RETURNING sender_name, recipient, destination, pickup, username'''\
			.format(sender_name, recipient, destination, pickup, weight, username))

		orders = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()

		return orders


	def get_all_parcels(self):

		self.curr.execute(''' SELECT * FROM orders''')
	

		orders = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()

		return json.dumps(orders, default=str)

	
	def get_one_parcel(self, parcel_id):

		self.curr.execute(''' SELECT * FROM orders WHERE id=%s''',(parcel_id, ))

		order = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()

		if order:
			return self.objectify(order)
		return None

	
