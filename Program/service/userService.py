from Program.models.user import User


class userService:
    # 根据usernam查询name
    def getNameByUsername(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            return user.name
        else:
            return None

    # 验证用户名和密码匹配
    def checkUsernameAndPassword(self, data):
        username = data["username"]
        password = data["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        else:
            return None
