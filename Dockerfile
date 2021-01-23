FROM python:3.7-alpine
RUN apk update
RUN apk add --no-cache git openssh
WORKDIR /git-backup-s3
RUN mkdir backups

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY main.py .
CMD [ "python3", "main.py" ]
