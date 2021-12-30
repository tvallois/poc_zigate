from typing import Tuple
from flask import Blueprint, current_app
from flask.json import jsonify
from flask.wrappers import Response
from poc_zigate.devices.schemas import DeviceSchema, PropertyEnum, PropertiesSchema

app = Blueprint("devices", __name__, url_prefix="/devices")


@app.route("/start_inclusion_mode", methods=["POST"])
def start_inclusion_mode() -> Tuple[Response, int] | Response:
    if current_app.config["ZIGATE_CLIENT"].is_permitting_join():
        return jsonify({"message": "zigate already in inclusion mode"}), 400
    current_app.config["ZIGATE_CLIENT"].permit_join()
    return jsonify({"message": "success"})


@app.route("/", methods=["GET"])
def get_devices() -> Response:
    current_app.config["ZIGATE_CLIENT"].get_devices_list()
    return jsonify(DeviceSchema(many=True).dump(current_app.config["ZIGATE_CLIENT"].devices))


@app.route("/<string:addr_device>/<string:property_name>")
def get_property_by_name(addr_device: str, property_name: str) -> Tuple[Response, int] | Response:
    valid_property_values = [p.value for p in PropertyEnum]
    if property_name not in valid_property_values:
        return (
            jsonify(
                {
                    "message": "{} is invalid. Valid property names are {}".format(
                        property_name, ", ".join(valid_property_values)
                    )
                }
            ),
            400,
        )
    device = current_app.config["ZIGATE_CLIENT"].get_device_from_addr(addr_device)
    if not device:
        return (
            jsonify(
                {"message": "device with address {} does not exist".format(addr_device)},
            ),
            400,
        )
    current_app.config["ZIGATE_CLIENT"].refresh_device(device.addr)
    return jsonify(PropertiesSchema().dump(device.get_property(property_name)))
