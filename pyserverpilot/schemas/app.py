from marshmallow import Schema, fields


class WordpressSchema(Schema):
    site_title = fields.Str(required=True)
    admin_user = fields.Str(required=True)
    admin_password = fields.Str(required=True, validate=lambda p: 8 < p < 200)
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
