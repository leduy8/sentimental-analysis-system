from main import db

from .base import BaseModel


class ReviewModel(BaseModel):
    """Review Model"""

    __tablename__ = "reviews"

    platform = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Date, nullable=False)
    platform_specific = db.Column(db.Text, nullable=True)

    def __str__(self) -> str:
        return f"<ReviewModel {self.id}>"
