from Program.common.extends import db
from Program.models.suggestion import Suggestion
from Program.models.user import User
from Program.models.workprogress import HomeworkProgress


class SuggestionService:
    # 根据学号查询name和department
    def getNameByUsername(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            return user.name, user.department
        else:
            return None

    # 根据id查询意见
    def getById(self, id):
        suggestion = Suggestion.query.filter_by(id=id).first()
        progresses = HomeworkProgress.query.filter_by(homework_id=id).all()
        if suggestion:
            progress_list = [progress.to_dict() for progress in progresses]
            responseData = {
                "detail": suggestion.to_dict(),
                "progressList": progress_list
            }
            return responseData
        else:
            return None

    # 保存意见
    def save(self, data):
        student_id = data['studentId']
        title = data['title']
        is_public = data['isPub']
        contact = data['contact']
        description = data['description']
        category_id = data['categoryId']
        suggestion = Suggestion(student_id=student_id, title=title, is_public=is_public, contact=contact, description=description, category_id=category_id)
        db.session.add(suggestion)
        db.session.commit()
        # 首次提交作业流程
        name, department = self.getNameByUsername(student_id)
        workprogress = HomeworkProgress(homework_id=suggestion.id, department=department, name=name, content='首次留下作业')
        db.session.add(workprogress)
        db.session.commit()
        return suggestion.id

    # 获取意见列表
    def getList(self):
        suggestions = Suggestion.query.order_by(Suggestion.created_at.desc()).all()
        suggestionsList = []
        for s in suggestions:
            user = User.query.filter_by(username=s.student_id).first()
            name = user.name if user else None
            suggestion_dict = s.to_dict()
            suggestion_dict['name'] = name
            suggestionsList.append(suggestion_dict)
        return suggestionsList
