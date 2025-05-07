from flask import Blueprint, abort, make_response, request
from app.models.author import Author
from ..db import db, migrate
from .routes_utilities import validate_model, create_model, get_models_with_filters

authors_bp = Blueprint ("authors_bp", __name__, url_prefix="authors")

@authors_bp.get("")
def get_all_authors():
    # query = db.select(Author)

    # name_param = request.args.get("name")
    # if name_param:
    #     query = query.where(Author.name.ilike(f"%{name_param}%"))
    
    # authors = db.session.scalars(query.order_by(Author.id))

    # authors_response = [author.to_dict() for author in authors]   
    
    # return authors_response
    return get_models_with_filters(Author, request.args)


@authors_bp.get("/<author_id>/books")
def get_books_by_author(id):
    author = validate_model(Author, id)
    response = [book.to_dict() for book in author.books]
    return response


@authors_bp.post("")
def create_new_author():
    request_body = request.get_json()
    return create_model(Author, request_body)


@authors_bp.post("/<author_id>/books")
def create_book_with_author(author_id):
    author = validate_model(Author, author_id)
    
    request_body = request.get_json()
    request_body["author_id"] = author.id

    return create_model(Book, request_body)
