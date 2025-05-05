from flask import Blueprint, abort, make_response, request
from app.models.book import Book
from ..db import db


books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def post_new_book():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]

    new_book = Book(title=title, description=description)
    db.session.add(new_book)
    db.session.commit()

    response = dict(id=new_book.id, title=new_book.title, description=new_book.description) 

    return response, 201

@books_bp.get("")
def get_all_books():
    query = db.select(Book).order_by(Book.id)
    books = db.session.scalars(query)

    books_response = [dict(id=book.id, title=book.title, description=book.description) for book in books]
        
    return books_response

# @books_bp.get("/<id>")
# def get_one_book(id):
#     book = validate_id(id)

#     return dict(id=book.id, title=book.title, description=book.description)
        


def validate_id(id):
    try:
        id = int(id)
    except:
        response = {"message": f"book {id} invalid"}
        abort(make_response(response, 400))
    
    for book in books:
        if book.id == id:
            return book
        
    response = {"message": f"book {id} not found"}
    abort(make_response(response, 404))
