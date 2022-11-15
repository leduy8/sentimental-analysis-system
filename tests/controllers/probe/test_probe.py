import json

from tests.controllers import get_response_body_from_request
from tests.unittest_helper import BaseTestCaseWithClient


class ProbeTestCase(BaseTestCaseWithClient):
    def setUp(self):
        super().setUp()

    def test_probe_success_with_client(self):
        response = self.client.get("/ping")
        body = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(body, dict)

    def test_probe_success_with_helper_function(self):
        response, body = get_response_body_from_request(
            self.client, "/ping", None, "get"
        )
        response = self.client.get("/ping")
        body = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(body, dict)
