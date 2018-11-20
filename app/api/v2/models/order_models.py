from database import Database


class UsersModel(Database):         

	def __init__(self,username,email,password,user_role):
		super().__init__()
		self.username = username
		self.email = email
		self.password = password
		self.user_role = admin
		
	def save(self, sender_name, recipient, destination, pickup, weight, username):

		self.cursor.execute(
            ''' INSERT INTO users(username, email, password, user_role) VALUES(%s, %s,%s, %s)''',
            (self.username, self.email, self.password, self.admin))

		self.conn.commit()
		self.curr.close()

	def get_username(self, username):
		self.curr.execute(''' SELECT * FROM users WHERE username=%s''',(username, ))

		user = self.curr.fetchone()

		self.connection.commit()
		self.curr.close()

		if user:
			return self.objectify_user(user)
		return None

	def get_email(self, email):
		self.curr.execute(''' SELECT * FROM users WHERE email=%s''',(email, ))

		user = self.curr.fetchone()

		self.conn.commit()
		self.curr.close()

		if user:
			return self.objectify_user(user)
		return None

	def objectify_user(self, data):

		self.id = data[0]
		self.username = data[1]
		self.email = data[2]
		self.password = data[3]
		self.user_role = data[4]

		return self

class OrdersModel(Database):
	def __init__(self,sender_name=None,recipient=None,destination=None,pickup=None,weight=None,username=None):
		super().__init__()
		self.sender_name = sender_name
		self.recipient = recipient
		self.destination = destination
		self.pickup = pickup
		self.weight = weight
		self.username = username

	def save(self):

		self.curr.execute(
			''' INSERT INTO orders(sender_name,recipient,destination,pickup,weight,username) VALUES(%s, %s, %s,%s, %s, %s)''',
			(self.sender_name, self.recipient, self.destination, self.pickup,
				self.weight, self.username))

		self.conn.commit()
		self.curr.close()

	def get_order(self, parcel_id):

		self.curr.execute(''' SELECT * FROM orders WHERE id=%s''',(parcel_id, ))

		order = self.curr.fetchone()

		self.conn.commit()
		self.curr.close()

		if order:
			return self.objectify(order)
		return None
