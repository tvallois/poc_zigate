import os
from poc_zigate.application import create_flask_app

environment = os.environ.get("POC_ZIGATE_ENV", "development")
app = create_flask_app(environment)
