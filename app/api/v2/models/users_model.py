from app.api.v2.models.database import Database
from werkzeug.security import generate_password_hash

class UsersModel(Database):
	"""Initialization."""

	def __init__(self,username=None,email=None,password=None,admin=False):

		super().__init__()
		self.username = username
		self.email = email
		if password:
		    self.password = generate_password_hash(password)
		self.admin = admin

	def save(self,username,email,password, admin):
		"""Save information of the new user"""

		self.curr.execute(
            ''' INSERT INTO users(username, email, password, admin)\
             VALUES('{}','{}','{}','{}') RETURNING username, email, password, admin'''\
            .format(username,email,password,admin))
		create = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return create

	def get_username(self, username):
		"""Get user with specific username"""

		self.curr.execute(""" SELECT * FROM users WHERE username='{}'""".format(username,))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user

	def get_email(self, email):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT * FROM users WHERE email=%s''',(email, ))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user


