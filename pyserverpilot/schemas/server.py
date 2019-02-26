from marshmallow import Schema, fields


class UpdateServerSchema(Schema):
    plan = fields.Str(validate=lambda p: p in ['economy', 'business', 'first_class'])
    firewall = fields.Bool()
    autoupdates = fields.Bool()
    deny_unknown_domains = fields.Bool()
