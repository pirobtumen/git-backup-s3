# Git backup to S3

Backup your Git repositories to S3 easily using a Python (Docker) script.

## Why

I run my own private Gitlab (on-premise). I want to have a security backup of my private projects,
but I want a script that is fully automatic. The task can be run using a Cron, or inside a k8s
cluster (CronJob) with Docker.

I don't mind if the MRs/Comments are lost, I just want an external backup of the source code.

> Requires Docker installed.

## Set up

## 1. Create gitlab personal access token

https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

## 2. Create a AWS S3 bucket

TODO :D

## 3. Environment

Set up your environment variables inside `.env` file:

```
GIT_USER=
GIT_TOKEN=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=
AWS_REGION=
```

Create the file `repos.json`:

```
[
    "gitlab.com/<user>/<repo>.git",
    "gitlab.com/<user>/<repo2>.git",
    "gitlab.com/<user>/<repo3>.git",
    ...
]
```

## 4. Run locally

```
$ make run
```
