from flask import Blueprint, abort, make_response, request
from app.models.book import Book
from ..db import db
from .routes_utilities import validate_model, create_model, get_models_with_filters


books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def post_new_book():
    request_body = request.get_json() 
    return create_model(Book, request_body)

@books_bp.get("")
def get_all_books():
    # query = db.select(Book).order_by(Book.id)
    # books = db.session.scalars(query)

    # books_response = [dict(id=book.id, title=book.title, description=book.description) for book in books]
        
    # return books_response
    return get_models_with_filters(Book, request.args)

@books_bp.get("/<id>")
def get_one_book(id):
    book = validate_model(Book, id)

    return dict(id=book.id, title=book.title, description=book.description)
        



