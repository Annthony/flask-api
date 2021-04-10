from flask import Flask, jsonify, request

from hejnote.model.item import Item, ItemSchema
from hejnote.model.note import Note, NoteSchema
from hejnote.model.todo import Todo, TodoSchema
from hejnote.model.item_type import ItemType

app = Flask(__name__)

items = [
    Note('Note 1', 'The body of note 1'),
    Note('Note 2', 'The body of note 2'),
    Todo('Todo 1', 'The body of todo 1'),
    Todo('Todo 2', 'The body of todo 2'),
]


@app.route('/item')
def get_items():
    schema = ItemSchema(many=True)
    return schema.dumps(items)


@app.route('/note')
def get_notes():
    schema = NoteSchema(many=True)
    notes = schema.dumps(
        filter(lambda i: i.type == ItemType.NOTE, items)
    )

    return notes


@app.route('/note', methods=['POST'])
def add_note():
    note = NoteSchema().load(request.get_json())
    items.append(notes)
    return "", 204


@app.route('/todo')
def get_todos():
    schema = TodoSchema(many=True)
    todos = schema.dumps(
        filter(lambda i: i.type == ItemType.TODO, items)
    )

    return todos