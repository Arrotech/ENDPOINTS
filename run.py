from app import parcel_app
from app.api.v2.models.database import Database

app = parcel_app()

@app.cli.command()
def create():
	Database().create_table()

@app.cli.command()
def destroy():
	Database().destroy_table()


if __name__ == "__main__":
	app.run(debug=True)
