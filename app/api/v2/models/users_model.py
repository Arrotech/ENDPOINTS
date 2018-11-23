from app.api.v2.models.database import Database
from flask_jwt_extended import jwt_required



class UsersModel(Database): 

	
	def __init__(self,username=None,email=None,password=None,check_admin=None):
		super().__init__()
		self.username = username
		self.email = email
		self.password = password
		self.check_admin = check_admin

	
	def save(self,username,email,password,check_admin):


		self.curr.execute(
            ''' INSERT INTO users(username, email, password, check_admin)\
             VALUES('{}','{}','{}','{}') RETURNING username, email, password, check_admin'''\
            .format(username,email,password,check_admin))
		create = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return create


	def get_username(self, username):

		self.curr.execute(""" SELECT * FROM users WHERE username='{}'""".format(username))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user

	def get_email(self, email):

		self.curr.execute(''' SELECT * FROM users WHERE email=%s''',(email, ))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user


