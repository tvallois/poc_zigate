from flask import Blueprint
from flask.json import jsonify
from flask.wrappers import Response
from poc_zigate import zigate_client
from poc_zigate.devices.schemas import DeviceSchema

app = Blueprint("devices", __name__, url_prefix="/devices")


@app.route("/start_inclusion_mode", methods=["POST"])
def start_inclusion_mode() -> Response:
    if zigate_client.is_permitting_join():
        return jsonify({"message": "zigate already in inclusion mode"})
    zigate_client.permit_join()
    return jsonify({"message": "success"})


@app.route("/", methods=["GET"])
def get_devices() -> Response:
    zigate_client.get_devices_list()
    return jsonify({"data": DeviceSchema(many=True).dumps(zigate_client.devices)})
