from main import db
from main.models.comment import CommentModel


def create_comment(data: dict) -> CommentModel:
    comment = CommentModel(content=data["content"])

    db.session.add(comment)
    db.session.commit()

    return comment
