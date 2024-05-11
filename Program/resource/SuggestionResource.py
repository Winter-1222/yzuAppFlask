# 保存意见表接口
from flask import request, jsonify
from flask_restful import Resource

from Program.common.R import Res
from Program.common.extends import api
from Program.service.suggestionService import SuggestionService


class saveSuggestionResource(Resource):
    def post(self):
        data = request.json
        res = SuggestionService().save(data)
        if res:
            return jsonify(Res.ok().set_message("保存成功").to_dict())
        else:
            return jsonify(Res.error().set_message("保存失败").to_dict())


api.add_resource(saveSuggestionResource, '/suggestion/save')
