from database import Database




if __name__ == '__main__':
    Database().destroy_table()
    Database().create_table()