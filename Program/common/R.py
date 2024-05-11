from Program.common.ResultCodeEnum import ResultCodeEnum

class Res:
    def __init__(self):
        self.success = None
        self.code = None
        self.message = None
        self.data = {}

    @staticmethod
    def ok():
        r = Res()
        r.set_success(ResultCodeEnum.SUCCESS.success)
        r.set_code(ResultCodeEnum.SUCCESS.code)
        r.set_message(ResultCodeEnum.SUCCESS.message)
        return r

    @staticmethod
    def error():
        r = Res()
        r.set_success(ResultCodeEnum.UNKNOWN_REASON.success)
        r.set_code(ResultCodeEnum.UNKNOWN_REASON.code)
        r.set_message(ResultCodeEnum.UNKNOWN_REASON.message)
        return r

    @staticmethod
    def set_result(result_code_enum):
        r = Res()
        r.set_success(result_code_enum.success)
        r.set_code(result_code_enum.code)
        r.set_message(result_code_enum.message)
        return r

    def set_success(self, success):
        self.success = success
        return self

    def set_message(self, message):
        self.message = message
        return self

    def set_code(self, code):
        self.code = code
        return self

    def add_data(self, key, value):
        self.data[key] = value
        return self

    def data_dict(self, data_dict):
        self.data = data_dict
        return self

    def to_dict(self):
        return {"success": self.success, "code": self.code, "message": self.message, "data": self.data}
