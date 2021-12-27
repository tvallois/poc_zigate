from flask import Blueprint, current_app
from flask.json import jsonify
from flask.wrappers import Response
from poc_zigate.devices.schemas import DeviceSchema

app = Blueprint("devices", __name__, url_prefix="/devices")


@app.route("/start_inclusion_mode", methods=["POST"])
def start_inclusion_mode() -> Response:
    if current_app.config["ZIGATE_CLIENT"].is_permitting_join():
        return jsonify({"message": "zigate already in inclusion mode"})
    current_app.config["ZIGATE_CLIENT"].permit_join()
    return jsonify({"message": "success"})


@app.route("/", methods=["GET"])
def get_devices() -> Response:
    current_app.config["ZIGATE_CLIENT"].get_devices_list()
    return jsonify(DeviceSchema(many=True).dump(current_app.config["ZIGATE_CLIENT"].devices))
