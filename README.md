## A sample RESTful API with Python and Flask

### Running the API

To run this application, you will need Python 3+ and [Pipenv](https://pipenv.readthedocs.io/en/latest/) installed locally. If you have then, you can issue the following commands:

```bash
# from the flask-api directory
pipenv install
./bootstrap.sh 
```

### Running the API with Docker
# build the image
```bash
docker build -t hejnote .
```

# run a new docker container named hejnote
```bash
docker run --name hejnote -d -p 5000:5000 hejnote
```

# fetch items from the dockerized instance
```bash
Visit http://localhost:5000/api/item
```