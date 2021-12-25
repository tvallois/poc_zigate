from typing import cast
import zigate


zigate_client = cast(zigate.ZiGateGPIO, zigate.connect(port="auto", gpio=True))
