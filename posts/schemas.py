from marshmallow import Schema, fields, validate
from users import UserSchema


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    status = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    author_id = fields.Int(load_only=True)
    author = fields.Nested(UserSchema(only=("id", "first_name", "last_name")), dump_only=True)