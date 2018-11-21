from app.api.v2.models.database import Database


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

	def get_all_parcels(self, sender_name, recipient, destination, pickup, weight, username):

		self.curr.execute(
			''' SELECT * FROM orders(sender_name,recipient,destination,pickup,weight,username)\
		 	WHERE('{}','{}','{}','{}','{}','{}') RETURNING sender_name, recipient, destination, pickup, username'''\
			.format(sender_name, recipient, destination, pickup, weight, username))

		orders = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()

		return orders

	

	def get_one_parcel(self, parcel_id):

		self.curr.execute(''' SELECT * FROM orders WHERE id=%s''',(parcel_id, ))

		order = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()

		if order:
			return self.objectify(order)
		return None

	'''def objectify(self, data):
        order = Order(username=data[1],destination=data[2],name=data[3],price=data[4],status=data[5])
        order.id = data[0]
        order.date = str(data[6])
        self = order
        return self
		return None'''
