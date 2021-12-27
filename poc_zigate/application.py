import os
from typing import Any, Dict, cast
from flask import Flask
from werkzeug.utils import import_string
import zigate


def create_flask_app(environment: str, test_mapping: Dict[str, Any] | None = None) -> Flask:
    app = Flask(__name__)

    with app.app_context():
        app.env = environment
        if environment == "test":
            if test_mapping is None:
                raise Exception("mapping must be defined for tests")
            setup_test_environment(app, test_mapping)
        else:
            setup_production_environment(app)
        register_blueprints(app)

    return app


def setup_test_environment(app: Flask, test_mapping: Dict[str, Any]) -> None:
    app.config.from_mapping(test_mapping)


def setup_production_environment(app: Flask) -> None:
    app.config.from_mapping(
        {"zigate_client": cast(zigate.ZiGateGPIO, zigate.connect(port="auto", gpio=True, path=None))}
    )


def register_blueprints(app: Flask) -> None:
    root_folder = "poc_zigate"

    for dir_name, _, _ in os.walk(root_folder):
        module_name = ("{}{}").format(dir_name.replace(os.path.sep, "."), ".views")
        module_path = os.path.join(dir_name, "views.py")

        if os.path.exists(module_path):
            module = import_string(module_name)
            obj = getattr(module, "app", None)
            if obj:
                app.register_blueprint(obj)
