import requests

from main import app
from main.engines.review import create_review
from main.utils.log import logging

logger = logging.Logger("Seed")


def create_seed_reviews(number_of_seeds: int = 20):
    headers = {"apikey": "ae818570-6496-11ed-bf86-b7eb9e8652ef"}

    params = (
        ("url", "https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P978C2R"),
        ("amount", str(number_of_seeds)),
    )

    response = requests.get(
        "https://app.reviewapi.io/api/v1/reviews", headers=headers, params=params
    )
    print(response.json())
    response_json = response.json()
    for review in response_json["reviews"]:
        with app.app_context():
            create_review(review)

    logger.info("Seed completed for reviews!")


def create_all_seeds():
    create_seed_reviews(number_of_seeds=1)


create_all_seeds()
