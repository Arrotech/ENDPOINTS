from app.api.v2.models.database import Database


class UsersModel(Database):         

	def __init__(self,username=None,email=None,password=None):
		super().__init__()
		self.username = username
		self.email = email
		self.password = password
		
	def save(self,username,email,password):

		self.curr.execute(
            ''' INSERT INTO users(username, email, password) VALUES('{}','{}','{}')RETURNING username, email, password'''\
            .format(username,email,password))

		self.conn.commit()
		self.curr.close()

		return self.curr.fetchone()

	def get_username(self, username):
		self.curr.execute(''' SELECT * FROM users WHERE username=%s''',(username, ))

		user = self.curr.fetchone()

		self.conn.commit()
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

