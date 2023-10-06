from marshmallow import Schema, fields, validate, post_load
from marshmallow_enum import EnumField
from .models import User
from app.constants import UserType
from .utils import validate_password
from app.blueprints.posts.schemas import PostSchema


class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # dump_only means that this field is for output only, not for input
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.Str(required=True, load_only=True, validate=validate_password)  # load_only means that this field is for input only, not for output
    user_type = EnumField(UserType, by_value=True, required=True, default=UserType.READER)
    is_active = fields.Bool(default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    posts = fields.List(fields.Nested(PostSchema(only=("id", "title")), dump_only=True))

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)