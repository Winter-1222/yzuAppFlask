import secrets
import string

from flask import jsonify, json, request
from flask_restful import Resource
from Program.common.ResultCodeEnum import ResultCodeEnum
from Program.common.R import Res
from Program.common.extends import api
from Program.service.userService import userService

# 登录接口
class LoginResource(Resource):
    def post(self):
        data = request.json
        print(data)
        user = userService().checkUsernameAndPassword(data)
        if user:
            token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(20))
            return jsonify(Res.ok().data_dict(user.to_dict()).add_data("token", token).to_dict())
        else:
            return jsonify(Res.error().set_message("账号或密码错误").to_dict())


api.add_resource(LoginResource, '/user/login')
