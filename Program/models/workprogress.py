from Program.common.extends import db
from datetime import datetime

class HomeworkProgress(db.Model):
    __tablename__ = 'homework_progress'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    homework_id = db.Column(db.Integer, nullable=False, comment='作业ID')
    department = db.Column(db.String(100), nullable=False, comment='部门')
    name = db.Column(db.String(100), nullable=False, comment='姓名')
    content = db.Column(db.Text(), nullable=False, comment='内容')
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='创建时间')

    def __repr__(self):
        return f"<HomeworkProgress(id={self.id}, homework_id='{self.homework_id}', department='{self.department}', name='{self.name}', content='{self.content}', created_at='{self.created_at}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'homework_id': self.homework_id,
            'department': self.department,
            'name': self.name,
            'content': self.content,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
