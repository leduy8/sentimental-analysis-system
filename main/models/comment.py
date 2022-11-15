from main import db

from .base import BaseModel


class CommentModel(BaseModel):
    """Comment Model"""

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    def __str__(self) -> str:
        return f"<CommentModel {self.id}>"
