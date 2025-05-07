from flask import Flask
from .db import db, migrate
from .models import book, author
from .routes.book_routes import books_bp
from .routes.author_routes import authors_bp
import os


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)

    return app