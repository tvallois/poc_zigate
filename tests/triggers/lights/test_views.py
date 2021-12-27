import unittest
from unittest.mock import Mock

import zigate
from poc_zigate.application import create_flask_app


class TriggerLightsViewTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_zigate_client = Mock()
        self.app = create_flask_app("test", {"TESTING": True, "ZIGATE_CLIENT": self.mock_zigate_client})

    def test_switch_on(self) -> None:
        with self.app.test_client() as client:
            mock_action_onoff = Mock()
            mock_device = Mock(action_onoff=mock_action_onoff)
            mock_get_device_from_addr = Mock(return_value=mock_device)
            self.mock_zigate_client.get_device_from_addr = mock_get_device_from_addr
            response = client.post("/triggers/lights/switch_on/mock_addr")
            assert response.json == {"message": "success"}
            mock_action_onoff.assert_called_once_with(zigate.ON)
            mock_get_device_from_addr.assert_called_once_with("mock_addr")

    def test_switch_on_with_unknown_device(self) -> None:
        with self.app.test_client() as client:
            mock_get_device_from_addr = Mock(return_value=None)
            self.mock_zigate_client.get_device_from_addr = mock_get_device_from_addr
            response = client.post("/triggers/lights/switch_on/mock_addr")
            assert response.json == [{"message": "device with address mock_addr does not exist"}, 400]
            mock_get_device_from_addr.assert_called_once_with("mock_addr")

    def test_switch_off(self) -> None:
        with self.app.test_client() as client:
            mock_action_onoff = Mock()
            mock_device = Mock(action_onoff=mock_action_onoff)
            mock_get_device_from_addr = Mock(return_value=mock_device)
            self.mock_zigate_client.get_device_from_addr = mock_get_device_from_addr
            response = client.post("/triggers/lights/switch_off/mock_addr")
            assert response.json == {"message": "success"}
            mock_action_onoff.assert_called_once_with(zigate.OFF)
            mock_get_device_from_addr.assert_called_once_with("mock_addr")

    def test_switch_off_with_unknown_device(self) -> None:
        with self.app.test_client() as client:
            mock_get_device_from_addr = Mock(return_value=None)
            self.mock_zigate_client.get_device_from_addr = mock_get_device_from_addr
            response = client.post("/triggers/lights/switch_off/mock_addr")
            assert response.json == [{"message": "device with address mock_addr does not exist"}, 400]
            mock_get_device_from_addr.assert_called_once_with("mock_addr")
