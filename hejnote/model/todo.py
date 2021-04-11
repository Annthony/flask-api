from marshmallow import post_load

from .item import Item, ItemSchema
from .item_type import ItemType


class Todo(Item):
    def __init__(self, title, body):
        super(Todo, self).__init__(title, body, ItemType.TODO)

    def __repr__(self):
        return '<Todo(name={self.title!r})>'.format(self=self)


class TodoSchema(ItemSchema):
    @post_load
    def make_todo(self, data, many, **kwargs):
        return Todo(**data)