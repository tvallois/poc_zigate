from enum import Enum
from marshmallow import Schema, fields


class InfoSchema(Schema):
    addr = fields.String(required=True, dump_only=True)
    ieee = fields.String(required=True, dump_only=True)
    lqi = fields.Int(strict=True, required=True, dump_only=True)
    mac_capability = fields.String(required=True, dump_only=True)
    last_seen = fields.String(required=True, dump_only=True)


class PropertiesSchema(Schema):
    name = fields.String(required=True, dump_only=True)
    attribute = fields.Int(required=True, dump_only=True, strict=True)
    data = fields.Raw(required=True, dump_only=True)


class DeviceSchema(Schema):
    info = fields.Nested(InfoSchema, required=True, dump_only=True)
    missing = fields.Boolean(required=True, dump_only=True)
    discovery = fields.String(required=True, dump_only=True)
    properties = fields.Nested(PropertiesSchema, required=True, dump_only=True, many=True)


class PropertyEnum(Enum):
    manufacturer = "manufacturer"
    colour_temperature = "colour_temperature"
    onoff = "onoff"
    current_level = "current_level"
