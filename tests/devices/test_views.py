import unittest
from unittest.mock import Mock
from poc_zigate.application import create_flask_app


class DeviceViewTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_zigate_client = Mock()
        self.app = create_flask_app("test", {"TESTING": True, "ZIGATE_CLIENT": self.mock_zigate_client})

    def test_get_devices(self) -> None:
        with self.app.test_client() as client:
            self.mock_zigate_client.devices = {"oui": "non"}
            response = client.get("/devices/")
            print(response.json)
