from Program.common.extends import db
from Program.models.workprogress import HomeworkProgress


class workProgressService:
    def save(self, data):
        print(data)
        homeworkId = data['homeworkID']
        department = data['department']
        name = data['name']
        content = data['content']
        progress = HomeworkProgress(homework_id=homeworkId, department=department, name=name, content=content)
        db.session.add(progress)
        db.session.commit()
        return progress.id
