import psycopg2
import os
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self):
    	self.db_name = os.getenv('DB_NAME')
    	self.db_host = os.getenv('DB_HOST')
    	self.db_user = os.getenv('DB_USER')
    	self.db_password = os.getenv('DB_PASSWORD')

    	self.conn = psycopg2.connect(database=self.db_name,host=self.db_host,user=self.db_user,password=self.db_password)

    	self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_table(self):
        queries = [
        	"""
	        CREATE TABLE IF NOT EXISTS users(
				user_id serial PRIMARY KEY,
				username varchar(50) NOT NULL,
				email varchar(50) NOT NULL,
				password varchar NOT NULL,
                check_admin varchar(50) NOT NULL DEFAULT 'User'
			)""",
			"""

			CREATE TABLE IF NOT EXISTS orders(
				parcel_id serial PRIMARY KEY,
				sender_name varchar(50) NOT NULL,
				recipient varchar(50) NOT NULL,
				destination varchar(50) NOT NULL,
				pickup varchar(50) NOT NULL,
				weight numeric NOT NULL,
				username varchar(50) NOT NULL,
                order_status varchar(50) NOT NULL DEFAULT 'In-Transit'
			)"""

        ]
        for query in queries:
        	self.curr.execute(query)

        self.conn.commit()
        self.curr.close()

    def destroy_table(self):
        orders = "DROP TABLE IF EXISTS  orders CASCADE"
        users = "DROP TABLE IF EXISTS  users CASCADE"
        queries = [orders,users]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e
