import psycopg2
from psycopg2 import Error
import os


	def connection(url):
		try:
			connection = psycopg2.connect(
				user="arrotech",
				password="Harun20930988!",
				host="localhost",
				database="postgres",
				port="5432"
				)

			return connection
		except (Exception, psycopg2.Error) as e:
			print("Error while connecting to the PostgreSQL", e)

	def init_db():
		connection = connection(url)
		return connection

	def create_table():
		conn = connection(url)
		curr = conn.cursor()
		queries = tables()
		for query in queries:
			curr.execute(query)
		conn.commit()
		
	def destroy_table():
		table = tables()
		conn = connection
		curr = conn.cursor()
		orders = "DROP TABLE IF EXISTS orders CASCADE"
		users = "DROP TABLE IF EXISTS users CASCADE"
		queries = [orders,users]
		for query in queries:
			curr.execute(query)
		conn.commit()

	def tables():
		users = """CREATE TABLE IF NOT EXISTS user(
			user_id serial PRIMARY KEY,
			username varchar(50) NOT NULL,
			email varchar(50) NOT NULL,
			password varchar(50) NOT NULL,
			user_role varchar(50) NOT NULL
			)"""

		orders = """CREATE TABLE IF NOT EXISTS orders(
			order_id serial PRIMARY KEY,
			order_name varchar(50) NOT NULL,
			sender_name varchar(50) NOT NULL,
			recipient varchar(50) NOT NULL,
			pickup varchar(50) NOT NULL,
			destination varchar(50) NOT NULL,
			price varchar(50) FLOAT NOT NULL,
			weight numeric NOT NULL,
			date_created timestamp with time zone DEFAULT('now'::text)::datetime
		)"""

		query = [users, orders]



"""finally:
	if(connection):
		cursor.close()
		connection.close()
		print("database connection has been closed successfully")"""
