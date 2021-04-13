FROM python:3.9-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /flask_api
COPY Pipfile Pipfile.lock __init__.py app.py bootstrap.sh ./
COPY hejnote ./hejnote
COPY tests ./tests

RUN pipenv install
RUN pipenv install --dev pytest
RUN pipenv run pytest

EXPOSE 5000
ENTRYPOINT ["/flask_api/bootstrap.sh"]