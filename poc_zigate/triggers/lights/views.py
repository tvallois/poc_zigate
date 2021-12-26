from flask import Blueprint, jsonify
from flask.wrappers import Response
import zigate
from poc_zigate import zigate_client

lights_blueprint = Blueprint("lights", __name__, url_prefix="/triggers/lights")


@lights_blueprint.route("/switch_on/<string:addr_device>", methods=["POST"])
def switch_on(addr_device: str) -> Response:
    device = zigate_client.get_device_from_addr(addr_device)
    if not device:
        return jsonify(
            (
                {
                    "message": "device with address {} does not exist".format(
                        addr_device
                    )
                },
                400,
            )
        )
    device.action_onoff(zigate.ON)
    return jsonify({"message": "success"})


@lights_blueprint.route("/switch_off/<string:addr_device>", methods=["POST"])
def switch_off(addr_device: str) -> Response:
    device = zigate_client.get_device_from_addr(addr_device)
    if not device:
        return jsonify(
            (
                {
                    "message": "device with address {} does not exist".format(
                        addr_device
                    )
                },
                400,
            )
        )
    device.action_onoff(zigate.OFF)
    return jsonify({"message": "success"})
