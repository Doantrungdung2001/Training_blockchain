import uuid

from sanic import Blueprint
from sanic.response import json

from app.databases.mongodb import MongoDB
from app.decorators.json_validator import validate_with_jsonschema
from app.models.user import create_user_json_schema, User
from app.utils.jwt_utils import generate_jwt

user_bp = Blueprint('users_blueprint', url_prefix='/user')

_db = MongoDB()

@user_bp.route('/register', methods={'POST'})
@validate_with_jsonschema(create_user_json_schema)  # To validate request body
async def register_user(request):
    body = request.json

    user_id = str(uuid.uuid4())
    user = User(user_id).from_dict(body)

    check = _db.get_user(user.username,user.password)
    if(check is None):
        # # TODO: Save users to database
        register = _db.create_user(user)
        token = generate_jwt(user.username)

        return json({
            'status': 'success',
            'users': register.to_dict(),
            'token': token
        })
    else:
        return json({
            'status': 'Account is existing'
        })



@user_bp.route('/login', methods={'POST'})
@validate_with_jsonschema(create_user_json_schema)  # To validate request body
async def login_user(request):
    body = request.json
    user = User().from_dict(body)

    login = _db.get_user(user.username,user.password)
    token = generate_jwt(user.username)
    print(login)
    if(login):
        return json({
            'status': 'login success',
            'users': login,
            'token': token
        })
    else:
        return json({
            'status': 'login fail'
        })