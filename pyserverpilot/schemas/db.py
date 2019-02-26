import re

from marshmallow import Schema, fields


class UserSchema(Schema):
    # Length must be at most 16 characters.
    name = fields.Str(required=True, validate=lambda n: len(n) <= 16)

    # No leading or trailing whitespace and the password must be at between 8 and 200 characters long
    password = fields.Str(required=True, validate=lambda p: p[0] != ' ' and p[-1] != ' ' and 8 <= p <= 200)


class CreateDBSchema(Schema):
    appid = fields.Str(required=True)

    # Length must be between 3 and 64 characters.
    # Characters can be of lowercase ascii letters, digits, or a dash ('abcdefghijklmnopqrstuvwxyz0123456789-').
    name = fields.Str(required=True, validate=lambda n: 3 < len(n) < 64 and re.match(re.compile(r'^[-a-zA-Z0-9]+$'), n))

    user = fields.Nested(UserSchema, required=True)


class UpdateDBSchema(Schema):
    user = fields.Nested(UserSchema, required=True)
