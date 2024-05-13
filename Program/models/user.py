from Program.common.extends import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False, comment='账号')
    password = db.Column(db.String(100), nullable=False, comment='密码')
    name = db.Column(db.String(100), nullable=False, comment='姓名')
    role = db.Column(db.String(100), nullable=False, comment='角色')
    department = db.Column(db.String(100), nullable=False, comment='部门')  # 新添加的部门属性

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', name='{self.name}', role='{self.role}', department='{self.department}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'role': self.role,
            'department': self.department
        }
