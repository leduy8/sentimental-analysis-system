from main.models.base import BaseModel


def find_object_model_by_id(id: int, model: BaseModel) -> BaseModel:
    """Find object model by ID

    Args:
        id (int): ID of object model
        model (BaseModel): Object Model that derives from BaseModel

    Returns:
        BaseModel: Object model or None
    """
    return model.query.get(id)
