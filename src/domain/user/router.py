from flask import request, jsonify
import domain.user.controller as Controller

def user_router(app):
    
    @app.route('/user', methods=['GET'])
    def get_users():
        list_user = Controller.get_all_user()
        return jsonify(list_user), 200

    @app.route('/user', methods=['POST'])
    def creat_user():
        body = request.get_json()
        print(body)
        new_user = Controller.create_user(body)
        return jsonify(new_user), 201