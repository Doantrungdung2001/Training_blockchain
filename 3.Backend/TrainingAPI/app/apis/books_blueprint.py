import uuid

from sanic import Blueprint
from sanic.response import json

from app.constants.cache_constants import CacheConstants
from app.databases.mongodb import MongoDB
from app.databases.redis_cached import get_cache, set_cache
from app.decorators.json_validator import validate_with_jsonschema
# from app.hooks.error import ApiInternalError
from app.models.book import create_book_json_schema, Book

books_bp = Blueprint('books_blueprint', url_prefix='/books')
# books_bp_id = Blueprint('books_blueprint', url_prefix='/books/<id>')
# books_update_id = Blueprint('books_blueprint', url_prefix='/books/<id>')
# books_delete_id = Blueprint('books_blueprint', url_prefix='/books/<id>')


_db = MongoDB()

@books_bp.route('/')
async def get_all_books(request):
    # # TODO: use cache to optimize api
    # async with request.app.ctx.redis as r:
    # books_cache = await get_cache(r, CacheConstants.all_books)
    # if books is None:
    #     book_objs = _db.get_books()
    #     books = [book.to_dict() for book in book_objs]
    #     await set_cache(r, CacheConstants.all_books, books)

    book_objs = _db.get_books()
    books = [book.to_dict() for book in book_objs]
    number_of_books = len(books)
    return json({
        'n_books': number_of_books,
        'books': books
    })

@books_bp.route('/<id>',methods={'GET'})
async def get_books_id(request, id):
    # # TODO: use cache to optimize api
    # async with request.app.ctx.redis as r:
    #     books = await get_cache(r, CacheConstants.all_books)
    #     if books is None:
    #         book_objs = _db.get_books()
    #         books = [book.to_dict() for book in book_objs]
    #         await set_cache(r, CacheConstants.all_books, books)
    #
    book_objs = _db.get_book_id(id)
    if(book_objs):
        return json({
            'status': 'success',
            'books': book_objs
        })
    else:
        return json({
            'status' : 'fail'
        })



@books_bp.route('<id>',methods={'PUT'})
async def update_books_id(request, id):
    # # TODO: use cache to optimize api
    # async with request.app.ctx.redis as r:
    #     books = await get_cache(r, CacheConstants.all_books)
    #     if books is None:
    #         book_objs = _d    b.get_books()
    #         books = [book.to_dict() for book in book_objs]
    #         await set_cache(r, CacheConstants.all_books, books)
    body = request.json

    book = Book(id).from_dict(body)

    # return json({
    #     'book': book.to_dict()
    # })
    book_objs = _db.update_book(id,book)

    if(book_objs):
        return json({
            'status': 'success',
            'books': book.to_dict()
        })
    else:
        return json({
            'status': 'fail'
        })

@books_bp.route('<id>',methods={'DELETE'})
async def delete_books_id(request, id):
    # # TODO: use cache to optimize api
    # async with request.app.ctx.redis as r:
    #     books = await get_cache(r, CacheConstants.all_books)
    #     if books is None:
    #         book_objs = _db.get_books()
    #         books = [book.to_dict() for book in book_objs]
    #         await set_cache(r, CacheConstants.all_books, books)

    book_objs = _db.delete_book(id)
    if(book_objs):
        return json({
            'status': 'success',
        })
    else:
        return json({
            'status': 'fail'
        })



@books_bp.route('/', methods={'POST'})
# @protected  # TODO: Authenticate
@validate_with_jsonschema(create_book_json_schema)  # To validate request body
async def create_book(request, username=None):
    body = request.json

    book_id = str(uuid.uuid4())
    book = Book(book_id).from_dict(body)
    book.owner = username

    # # TODO: Save book to database
    inserted = _db.add_book(book)

    # if not inserted:
    #     raise ApiInternalError('Fail to create book')

    # TODO: Update cache

    return json({
        'status': 'success',
        'books': book.to_dict(),
    })


# TODO: write api get, update, delete book
