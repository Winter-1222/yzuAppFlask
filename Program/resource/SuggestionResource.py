from flask import request, jsonify
from flask_restful import Resource
from Program.common.R import Res
from Program.common.extends import api
from Program.service.suggestionService import SuggestionService


# 获取作业详情和进展
class getSuggestionByIdResource(Resource):
    def get(self):
        id = request.args.get("id")
        responseData = SuggestionService().getById(id)
        if responseData:
            return jsonify(Res.ok().set_message("获取成功").data_dict(responseData).to_dict())
        else:
            return jsonify(Res.error().set_message("失败").to_dict())
        pass


api.add_resource(getSuggestionByIdResource, '/suggestion/getById')


# 获取意见表接口
class getSuggestionResource(Resource):
    def get(self):
        list = SuggestionService().getList()
        if list:
            return jsonify(Res.ok().set_message("获取成功").data_dict(list).to_dict())
        else:
            return jsonify(Res.error().set_message("失败").to_dict())


api.add_resource(getSuggestionResource, '/suggestion/list')


# 保存意见表接口
class saveSuggestionResource(Resource):
    def post(self):
        data = request.json
        res = SuggestionService().save(data)
        if res:
            return jsonify(Res.ok().set_message("保存成功").to_dict())
        else:
            return jsonify(Res.error().set_message("保存失败").to_dict())


api.add_resource(saveSuggestionResource, '/suggestion/save')
