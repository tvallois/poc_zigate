from typing import cast
import zigate


class ZigateClient:
    def __init__(self):
        self._zigate: zigate.ZiGateGPIO | None = None

    def init_zigate_client(self):
        self._zigate = cast(zigate.ZiGateGPIO, zigate.connect(port="auto", gpio=True, path=None))
