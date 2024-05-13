from Program.common.extends import db
from datetime import datetime

class Suggestion(db.Model):
    __tablename__ = 'suggestions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(100), nullable=False, comment='学号')
    title = db.Column(db.String(255), nullable=False, comment='意见标题')
    is_public = db.Column(db.Boolean, default=False, nullable=False, comment='是否公开')
    contact = db.Column(db.String(100), nullable=False, comment='联系方式')
    description = db.Column(db.Text(), nullable=False, comment='问题描述')
    category_id = db.Column(db.Integer, nullable=False, comment='分类ID')
    status = db.Column(db.Boolean, default=False, nullable=False, comment='作业状态')
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False, comment='创建时间')

    def __repr__(self):
        return f"<Suggestion(id={self.id}, student_id='{self.student_id}', title='{self.title}', is_public='{self.is_public}', contact='{self.contact}', category_id='{self.category_id}', status='{self.status}', created_at='{self.created_at}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'title': self.title,
            'is_public': self.is_public,
            'contact': self.contact,
            'description': self.description,
            'category_id': self.category_id,
            'status': self.status,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
