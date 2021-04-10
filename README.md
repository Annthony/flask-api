## A sample RESTful API with Python and Flask

### Running the API

To run this application, you will need Python 3+ and [Pipenv](https://pipenv.readthedocs.io/en/latest/) installed locally. If you have then, you can issue the following commands:

```bash
# from the flask-api directory
pipenv install
./bootstrap.sh 
```

Then you can issue requests to your API. For example, with `curl`, you can issue requests like that:

```bash
# inserting a new hejnote
curl -X POST -H "Content-Type: application/json" -d '{
    "title": "A New Note,
    "note": "This is the body of the note."
}' http://localhost:5000/note

# listing all incomes
curl http://localhost:5000/note
```