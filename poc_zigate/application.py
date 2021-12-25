import os
from flask import Flask
from werkzeug.utils import import_string


def create_flask_app(environment: str) -> Flask:
    app = Flask(__name__)

    with app.app_context():
        app.env = environment
        register_blueprints(app)

    return app


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
