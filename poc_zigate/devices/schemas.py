from marshmallow import Schema, fields


class InfoSchema(Schema):
    addr = fields.String(required=True, dump_only=True)
    ieee = fields.String(required=True, dump_only=True)
    lqi = fields.Int(strict=True, required=True, dump_only=True)
    mac_capability = fields.String(required=True, dump_only=True)
    last_seen = fields.String(required=True, dump_only=True)


class DeviceSchema(Schema):
    info = fields.Nested(InfoSchema, required=True, dump_only=True)
    missing = fields.Boolean(required=True, dump_only=True)
    discovery = fields.String(required=True, dump_only=True)
