from flask import Blueprint
from poc_zigate import zigate_client

lights_blueprint = Blueprint("lights", __name__, url_prefix="/triggers")


@lights_blueprint.route("/switch_on/<string:addr_device>", methods=["POST"])
def switch_on(addr_device: str):
    pass
