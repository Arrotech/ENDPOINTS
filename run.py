from app import parcel_app
import os
from app.api.v2.models.database import Database

#config_name = os.getenv('APP_SETTINGS') # config_name = "development"
#app = parcel_app(config_name)

@app.cli.command()
def create():
	Database().create_table()

@app.cli.command()
def destroy():
	Database().destroy_table()

if __name__ == "__main__":
	app.run(debug=True)
