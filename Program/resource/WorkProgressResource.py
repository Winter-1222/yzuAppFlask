from flask import request, jsonify
from flask_restful import Resource


# 保存进展表接口
from Program.common.R import Res
from Program.common.extends import api
from Program.service.workProgressService import workProgressService


class saveProgressResource(Resource):
    def post(self):
        data = request.json
        res = workProgressService().save(data)
        if res:
            return jsonify(Res.ok().set_message("保存成功").to_dict())
        else:
            return jsonify(Res.error().set_message("保存失败").to_dict())


api.add_resource(saveProgressResource, '/progress/save')
