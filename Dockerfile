FROM python:3.9-alpine

RUN apk update
RUN apk add --no-cache git openssh

RUN addgroup -S python && adduser -S python -G python
WORKDIR /git-backup-s3
RUN mkdir backups
RUN chown -R python:python /git-backup-s3

USER python
COPY --chown=python:python requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY --chown=python:python main.py .
CMD [ "python3", "main.py" ]
