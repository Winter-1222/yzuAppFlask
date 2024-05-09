from flask import jsonify, json, request
from flask_restful import Resource
from Program.common.extends import api


class LoginResource(Resource):
    def post(self):
        data = request.json
        print(data)
        return {"code": 200}


api.add_resource(LoginResource, '/user/login')
