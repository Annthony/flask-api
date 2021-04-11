from flask import Flask, jsonify, request
from marshmallow.exceptions import ValidationError

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


@app.route('/api/item')
def get_items():
    schema = ItemSchema(many=True)
    return jsonify(schema.dump(items))


@app.route('/api/note') 
def get_notes():        
    schema = NoteSchema(many=True)
    notes = schema.dump(
        filter(lambda i: i.type == ItemType.NOTE, items)
    )

    return jsonify(notes)


@app.route('/api/note', methods=['POST'])
def add_note():
    try:
        note = NoteSchema().load(request.get_json())
        items.append(note)
        return "Note added", 200
    except ValidationError as err:
        return err.messages, 400


@app.route('/api/todo')
def get_todos():
    schema = TodoSchema(many=True)
    todos = schema.dump(
        filter(lambda i: i.type == ItemType.TODO, items)
    )

    return jsonify(todos)


@app.route('/api/todo', methods=['POST'])
def add_todo():
    try:
        todo = TodoSchema().load(request.get_json())
        items.append(todo)
        return "Todo added", 200
    except ValidationError as err:
        return err.messages, 400