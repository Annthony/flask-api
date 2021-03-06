from marshmallow import post_load

from .item import Item, ItemSchema
from .item_type import ItemType


class Note(Item):
    def __init__(self, title, body):
        super(Note, self).__init__(title, body, ItemType.NOTE)

    def __repr__(self):
        return '<Note(name={self.title!r})>'.format(self=self)


class NoteSchema(ItemSchema):
    @post_load
    def make_note(self, data, many, **kwargs):
        return Note(**data)