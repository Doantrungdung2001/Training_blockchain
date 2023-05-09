from pymongo import MongoClient
import datetime

from app.constants.mongodb_constants import MongoCollections
from app.models.book import Book
from app.models.user import User
from app.utils.logger_utils import get_logger
from config import MongoDBConfig

logger = get_logger('MongoDB')


class MongoDB:
    def __init__(self, connection_url=None):
        if connection_url is None:
            # connection_url = f'mongodb://{MongoDBConfig.USERNAME}:{MongoDBConfig.PASSWORD}@{MongoDBConfig.HOST}:{MongoDBConfig.PORT}'
            connection_url = 'mongodb://localhost:27017'
        # self.connection_url = connection_url.split('@')[-1]
        self.client = MongoClient(connection_url)
        self.db = self.client[MongoDBConfig.DATABASE]

        self._books_col = self.db[MongoCollections.books]
        self._users_col = self.db[MongoCollections.users]

        print("Connect is done!!!")
        print(self.client.list_database_names())
        print(self.db.list_collection_names())

    def get_books(self, filter_=None, projection=None):
        try:
            if not filter_:
                filter_ = {}
            cursor = self._books_col.find(filter_, projection=projection)
            data = []
            for doc in cursor:
                data.append(Book().from_dict(doc))
            return data
        except Exception as ex:
            logger.exception(ex)
        return []

    def get_book_id(self, id: str):
        try:
            # get_doc = self._books_col.find_one({"_id": id})
            # return get_doc
            if (book := self._books_col.find_one({"_id": id})):
                return book
        except Exception as ex:
            logger.exception(ex)
        return []

    # TODO: write functions CRUD with books
    def add_book(self, book: Book):
        try:
            inserted_doc = self._books_col.insert_one(book.to_dict())
            return inserted_doc
        except Exception as ex:
            logger.exception(ex)
        return None

    def update_book(self, id: str,book: Book):
        try:
            updated_doc = self._books_col.update_one({"_id": id}, {"$set": book.to_dict()})
            return updated_doc
            # if (book := self._books_col.find_one({"_id": id})) is not None:
            #     updated_doc = self._books_col.update_one({"_id": id}, {"$set": book.to_dict()})
            #     return updated_doc
        except Exception as ex:
            logger.exception(ex)
        return None

    def delete_book(self, id: str):
        try:
            # delete_doc = self._books_col.delete_one({"_id": id})
            if (book := self._books_col.find_one({"_id": id})) is not None:
                delete_doc = self._books_col.delete_one({"_id": id})
                return delete_doc
        except Exception as ex:
            logger.exception(ex)
        return None

    def create_user(self, user: User):
        try:
            inserted_user = self._users_col.insert_one(user.to_dict())
            return inserted_user
        except Exception as ex:
            logger.exception(ex)
        return None

    def get_user(self, username: str, password:str):
        try:
            if (user := self._users_col.find_one({"username": username},{"password": password})) is not None:
                return True
        except Exception as ex:
            logger.exception(ex)
        return False

    # # newBook = Book('0009')
    # db = MongoDB().add_book(newBook)


