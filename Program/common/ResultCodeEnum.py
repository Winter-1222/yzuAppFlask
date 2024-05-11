from enum import Enum


class ResultCodeEnum(Enum):
    SUCCESS = (True, 200, "成功")
    UNKNOWN_REASON = (False, 200, "未知错误")
    NO_TOKEN = (False, 208, "没有token")

    def __init__(self, success, code, message):
        self.success = success
        self.code = code
        self.message = message
