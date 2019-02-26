import re
import string

from marshmallow import Schema, fields


def validate_name(name: str) -> bool:
    """
    The name of the System User. Length must be between 3 and 32 characters. Characters can be of lowercase ascii
    letters, digits, or a dash ('abcdefghijklmnopqrstuvwxyz0123456789-'), but must start with a lowercase ascii letter.
    user-32 is a valid name, while 3po is not.
    """
    if 3 < len(name) < 32:
        return True

    if re.match(re.compile(r'^[-a-zA-Z0-9]+$'), name):
        return True

    if name[0] in string.ascii_lowercase:
        return True

    return False


class CreateSysUserSchema(Schema):
    serverid = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate_name)
    password = fields.Str(validate=lambda p: 8 < len(p) < 200)


class UpdateSysUserSchema(Schema):
    password = fields.Str(required=True, validate=lambda p: 8 < len(p) < 200)
