from marshmallow import Schema, fields


class WordpressSchema(Schema):
    site_title = fields.Str(required=True)
    admin_user = fields.Str(required=True)

    # Length must be between 8 and 200 characters
    admin_password = fields.Str(required=True, validate=lambda p: 8 < len(p) < 200)

    admin_email = fields.Str(required=True)


class CreateAppSchema(Schema):
    name = fields.Str(required=True)
    sysuserid = fields.Str(required=True)
    runtime = fields.Str(required=True)
    domains = fields.List(fields.Str(), required=False)
    wordpress = fields.Nested(WordpressSchema, required=False)


class UpdateAppSchema(Schema):
    runtime = fields.Str(required=False)
    domains = fields.List(fields.Str(), required=False)


class AddSSLSchema(Schema):
    key = fields.Str(required=True)
    cert = fields.Str(required=True)
    cacerts = fields.Str(required=True, default=None, allow_none=True)


class ForceSSLSchema(Schema):
    force = fields.Bool(required=True)
