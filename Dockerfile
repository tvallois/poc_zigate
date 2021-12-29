FROM python:alpine

RUN apk add --update \
    build-base \
    gcc \
    git \
    linux-headers \
    musl-dev


RUN pip install pipenv

WORKDIR /poc-zigate

ADD . /poc-zigate

RUN pipenv install --deploy

EXPOSE 8123

CMD ["pipenv", "run", "uwsgi", "--socket", "0.0.0.0:8123", "--protocol=http", "-w", "wsgi:app", "--enable-threads", "--thunder-lock", "--processes", "4", "--threads", "2"]