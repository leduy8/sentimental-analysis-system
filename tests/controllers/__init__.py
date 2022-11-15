import json


def get_response_body_from_request(client, url: str, data: dict, method: str):
    """CRUD request test function helper

    Args:
        client: Test client
        url (str): controller's URL
        data (dict): JSON data
        method (str): GET, POST, PUT, DELETE

    Returns:
        response: HTTP response | body: HTTP response body
    """
    response = getattr(client, method)(url, json=data)
    body = json.loads(response.get_data(as_text=True))
    return response, body


def get_response_body_from_request_form_data(client, url: str, data: dict, method: str):
    """CRUD request test function helper for form

    Args:
        client: Test client
        url (str): controller's URL
        data (dict): Form data? (Never use before)
        method (str): GET, POST, PUT, DELETE

    Returns:
        response: HTTP response | body: HTTP response body
    """
    response = getattr(client, method)(url, data=data, follow_redirects=True)
    body = json.loads(response.get_data(as_text=True))
    return response, body
