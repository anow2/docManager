from app import app
from pymongo import MongoClient
from app.services.database import client, db

if __name__ == '__main__':
    app.run()


@app.teardown_appcontext
def shutdown_session(exception=None):
    client.close()
