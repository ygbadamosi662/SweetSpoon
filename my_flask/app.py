from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from Blueprints.userController import user_bp
from Blueprints.AdminController import admin_bp
from config import Config
from models import storage


app = Flask(__name__)
app.config.from_object(Config)

jwt_manager = JWTManager(app)
ma = Marshmallow(app)

path_prefix = '/api/v1'

app.register_blueprint(user_bp, url_prefix=path_prefix+'/user')
app.register_blueprint(admin_bp, url_prefix=path_prefix+'/admin')


# with app.app_context():
#     secret = current_app.config.get('JWT_SECRET_KEY')
#     print(secret)

@app.route(path_prefix)
def home():
    # session = storage.get_session()
    # storage.deleteAll()
    # storage.close()
    # session.query(Student).delete()
    # session.commit()
    return jsonify("welcome home"), 200

if __name__ == '__main__':
    app.run()
