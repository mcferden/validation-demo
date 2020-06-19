from marshmallow import Schema, ValidationError, fields, post_load, validates

from entities import UserCreate


class BaseSchema(Schema):
    __entity_class__ = None

    @post_load
    def make_object(self, data, **kwargs):
        if self.__entity_class__:
            return self.__entity_class__(**data)
        return data


class TransactionSchema(Schema):
    id = fields.Integer()
    amount = fields.Decimal(as_string=True)


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    first_name = fields.String()
    last_name = fields.String()
    birth_date = fields.Date()
    transactions = fields.Nested(TransactionSchema, many=True)


class UserCreateSchema(BaseSchema):
    __entity_class__ = UserCreate

    email = fields.Email(required=True)
    password = fields.String(required=True)
    first_name = fields.String(missing=None)
    last_name = fields.String(missing=None)
    birth_date = fields.Date(missing=None)

    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('Password too short. Must be at least 8 characters.')
        required_characters = set('0123456789@#$&')
        if not set(value) & required_characters:
            raise ValidationError('Password must contain one of these: 0123456789@#$&')


user_schema = UserSchema()
user_create_schema = UserCreateSchema()
