from flask import Blueprint, jsonify, current_app
from flask.wrappers import Response
import zigate

app = Blueprint("lights", __name__, url_prefix="/triggers/lights")


@app.route("/switch_on/<string:addr_device>", methods=["POST"])
def switch_on(addr_device: str) -> Response:
    device = current_app.config["ZIGATE_CLIENT"].get_device_from_addr(addr_device)
    if not device:
        return jsonify(
            (
                {"message": "device with address {} does not exist".format(addr_device)},
                400,
            )
        )
    device.action_onoff(zigate.ON)
    return jsonify({"message": "success"})


@app.route("/switch_off/<string:addr_device>", methods=["POST"])
def switch_off(addr_device: str) -> Response:
    device = current_app.config["ZIGATE_CLIENT"].get_device_from_addr(addr_device)
    if not device:
        return jsonify(
            (
                {"message": "device with address {} does not exist".format(addr_device)},
                400,
            )
        )
    device.action_onoff(zigate.OFF)
    return jsonify({"message": "success"})
