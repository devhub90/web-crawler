from flask import Flask
from flask_migrate import Migrate, upgrade

from .extensions import db
from .views import main
from .utils import make_celery


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SECRET_KEY"] = "Oz8Z7Iu&DwoQK)g%*Wit2YpE#-46vy0n"
    app.config["CELERY_CONFIG"] = {"broker_url": "redis://redis", "result_backend": "redis://redis"}

    with app.app_context():
        db.init_app(app)
        migrate = Migrate(app, db)
        migrate.init_app(app, db)

    celery = make_celery(app)
    celery.set_default()

    app.register_blueprint(main)

    return app, celery
