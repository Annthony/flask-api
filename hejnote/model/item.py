import datetime as dt

from marshmallow import Schema, fields


class Item(object):
    def __init__(self, title, body, type):
        self.title = title
        self.body = body
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Item(name={self.title!r})>'.format(self=self)


class ItemSchema(Schema):
    title = fields.Str()
    body = fields.Str()
    created_at = fields.DateTime()
    type = fields.Str()