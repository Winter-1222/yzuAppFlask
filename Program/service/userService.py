from Program.models.user import User


class userService:
    # 验证用户名和密码匹配
    def checkUsernameAndPassword(self, data):
        username = data["username"]
        password = data["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        else:
            return None
