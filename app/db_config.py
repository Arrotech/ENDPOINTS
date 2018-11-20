import psycopg2

def connect():

    try:
    	
        conn = psycopg2.connect(user="postgres",host="localhost",password="postgres",database="postgres",port="5432")
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
    	print(error)
    