from Program.common.extends import db
from Program.models.suggestion import Suggestion


class SuggestionService:
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
        return suggestion.id
