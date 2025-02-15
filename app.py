from flask import Flask
from resources.cv import blp as CVBluePrint
from resources.ai import blp as AiBluePrint
from flask_smorest import Api
from db import db
from dotenv import load_dotenv
import os


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Chido REST API: Welcome To The Vortex"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(CVBluePrint)
    api.register_blueprint(AiBluePrint)

    return app


# Load environment variables
load_dotenv()
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Create the app instance
if all([USER, PASSWORD, HOST, PORT, DBNAME]):
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
else:
    DATABASE_URL = None

app = create_app(db_url=DATABASE_URL)


if __name__ == "__main__":
    app.run(debug=False)