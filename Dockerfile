FROM python:3.9-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /flask-api
COPY Pipfile Pipfile.lock __init__.py app.py bootstrap.sh ./
COPY hejnote ./hejnote
COPY tests ./tests

RUN pipenv install

EXPOSE 5000
ENTRYPOINT ["/flask-api/bootstrap.sh"]