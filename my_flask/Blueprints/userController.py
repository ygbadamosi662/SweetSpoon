from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from utility import util
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError
from schemas import user_schema, login_schema
from global_vars import globalBcrypt, USER
from models.user import User
from response_objects import getUserResponse
from Repos.userRepo import user_repo
from Enums.role import Role


user_bp = Blueprint('user', __name__)

@user_bp.route('/reg', methods=['POST'])
def reg():
    try:
        data = request.get_json()
        user_data = user_schema.load(data)

        # checks table integrity
        if util.validate_table_integrity_byEmail(user_data['email'], USER):
            return {'Message': '{} already exists'.format(user_data['email'])}, 400
        
        # # checks phone number uniqueness
        # if util.validate_table_integrity_byPhone(user_data['phone'], USER):
        #     return {'Message': '{} already exists'.format(user_data['phone'])}, 400
        
        user = User(first_name=user_data['first_name'], last_name=user_data['last_name'], gender=user_data['gender'], phone=user_data['phone'], email=user_data['email'], password=user_data['password'], role=Role.USER)

        util.persistModel(user)

        return jsonify(user_schema.dump(user_data)), 200     
    except ValidationError as err:
        return {'Error': repr(err)}, 400
    except TypeError as err:
        return {'Error': repr(err)}, 400
    except SQLAlchemyError as err:
        return {'Error': repr(err)}, 400
    finally:
        util.closeSession()

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        loginData = login_schema.load(data)

        if util.validate_table_integrity_byEmail(loginData['email'], USER) == False:
            return {'Message': 'Invalid Credentials'}

        user: User = user_repo.findByEmail(loginData['email'])

        if not user:
            return {'message': 'Invalid Credentials, only {} is allowed'.format(USER)}, 401

        if not globalBcrypt.checkpw(loginData['password'].encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({'message': 'Invalid Credentials'}), 401
        
        jwt_identity = {'email': loginData['email'], 'role': user.role.value}

        jwt = create_access_token(identity=jwt_identity)
        
        return jsonify({'jwt': jwt}), 201
    
    except ValidationError as err:
        return {'Error': repr(err)}, 400
    except TypeError as err:
        return {'Error': repr(err)}, 400
    except SQLAlchemyError as err:
        return {'Error': repr(err)}, 400
    finally:
        util.closeSession()
