from main import db
from main.models.review import ReviewModel


def create_review(data: dict) -> ReviewModel:
    review = ReviewModel(
        platform=data["platform"],
        rating=data["rating"],
        user_name=data["user_name"],
        text=data["text"],
        title=data["title"],
        timestamp=data["timestamp"],
    )

    if bool(data["platform_specific"]):
        review.platform_specific = str(data["platform_specific"])

    db.session.add(review)
    db.session.commit()

    return review
