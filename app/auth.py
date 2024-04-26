from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/anonymous-signin', methods=['POST'])
def anonymous_signin():
    print("In sign in function")
    json_data = request.get_json()
    anonymous_id = json_data['session_id']
    access_token = create_access_token(identity=anonymous_id)
    return jsonify(access_token=access_token)