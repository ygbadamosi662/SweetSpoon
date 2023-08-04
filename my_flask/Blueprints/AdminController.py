from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from utility import util
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError
from global_vars import REG_SUPER_A, USER
from models.user import User
from response_objects import getUserResponse
from Repos.userRepo import user_repo
from Enums.role import Role


admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/reg/super/<string:key>', methods=['GET'])
@jwt_required(optional=False)
def reg_super(key: str):
    try:
        user: User = util.getInstanceFromJwt()
        # validate user role
        if user.role == Role.SUPER_ADMIN:
            return {'Message': 'User already a super admin'}, 400
        
        if not key:
            return {'Message': 'key cannot be empty'}, 400
        
        # Validates key
        if key != REG_SUPER_A:
            return {'Message': 'invalid Credentials'}, 400
        
        user.role = Role.SUPER_ADMIN

        util.persistModel(user)

        return jsonify(getUserResponse(user)), 200
        
    except ValidationError as err:
        return {'Error': repr(err)}, 400
    except TypeError as err:
        return {'Error': repr(err)}, 400
    except SQLAlchemyError as err:
        return {'Error': repr(err)}, 400
    finally:
        util.closeSession()

@admin_bp.route('/reg/admin/<string:email>', methods=['GET'])
@jwt_required(optional=False)
def reg_admin(email: str):
    try:
        # validating user
        if get_jwt_identity()['role'] != Role.SUPER_ADMIN.value:
            return {'Message': 'Invalid Credentials'}, 400
        
        if not email:
            return {'Message': 'email cannot be emply'}, 400
        
        # validate email
        if util.validate_table_integrity_byEmail(email, USER) == False:
            return {'Message': 'User does not exist'}, 400
        
        admin: User = user_repo.findByEmail(email)
        # validate user role
        
        admin.role = Role.ADMIN

        util.persistModel(admin)

        return jsonify(getUserResponse(admin)), 200
    except ValidationError as err:
        return {'Error': repr(err)}, 400
    except TypeError as err:
        return {'Error': repr(err)}, 400
    except SQLAlchemyError as err:
        return {'Error': repr(err)}, 400
    finally:
        util.closeSession()
