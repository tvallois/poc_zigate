import unittest
from unittest.mock import Mock
from poc_zigate.application import create_flask_app


class DeviceViewTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_zigate_client = Mock()
        self.app = create_flask_app("test", {"TESTING": True, "ZIGATE_CLIENT": self.mock_zigate_client})

    def test_get_devices(self) -> None:
        with self.app.test_client() as client:
            devices = [
                {
                    "info": {
                        "addr": "mock_addr",
                        "ieee": "mock_ieee",
                        "lqi": 123456,
                        "mac_capability": "mock_mac_capability",
                        "last_seen": "2021-12-23 15:00:13",
                    },
                    "missing": False,
                    "discovery": "mock_discovery",
                }
            ]
            self.mock_zigate_client.devices = devices
            response = client.get("/devices/")
            assert response.json == devices
            self.mock_zigate_client.get_devices_list.assert_called_once_with()

    def test_start_inclusion_mode(self) -> None:
        with self.app.test_client() as client:
            mock_is_permitting_join = Mock(return_value=False)
            self.mock_zigate_client.is_permitting_join = mock_is_permitting_join
            response = client.post("/devices/start_inclusion_mode")
            assert response.json == {"message": "success"}
            mock_is_permitting_join.assert_called_once_with()

    def test_start_inclusion_mode_with_already_in_permitting_mode(self) -> None:
        with self.app.test_client() as client:
            mock_is_permitting_join = Mock(return_value=True)
            self.mock_zigate_client.is_permitting_join = mock_is_permitting_join
            response = client.post("/devices/start_inclusion_mode")
            assert response.json == {"message": "zigate already in inclusion mode"}
            mock_is_permitting_join.assert_called_once_with()
