import uuid

from sanic import Blueprint
from sanic.response import json

from app.databases.mongodb import MongoDB
from app.decorators.json_validator import validate_with_jsonschema
from app.models.user import create_user_json_schema, User

user_bp = Blueprint('users_blueprint', url_prefix='/user')

_db = MongoDB()

@user_bp.route('/', methods={'POST'})
@validate_with_jsonschema(create_user_json_schema)  # To validate request body
async def create_user(request):
    body = request.json

    user_id = str(uuid.uuid4())
    user = User(user_id).from_dict(body)

    # # TODO: Save book to database
    inserted = _db.create_user(user)

    # TODO: Update cache

    return json({
        'status': 'success!!!!!',
        'users': user.to_dict(),
    })

