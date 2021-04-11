FROM python:3.9-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY hejnote ./hejnote

RUN pipenv install

EXPOSE 5000
ENTRYPOINT ["/app/bootstrap.sh"]