<br />
<p align="center">

  <h2 align="center">Git Backup to S3 📦🚀☁️</h2>

  <p align="center">
    Backup multiple <b>Git</b> repositories at once to <b>S3</b> easily using a <i>Python script</i> with <b>Docker support</b>.
  </p>
</p>

## Why

I run my own private Gitlab (on-premise). I want a fully automatic periodic script that creates a security backup of my private projects, but just the source code, so it's fast and cheap.

## Features

- Tested sources: Gitlab, Github.
- Backup a list of repos at once.
- Requires HTTPS.
- The script zips each repo before uploading it to the cloud storage, so it will be cheap.

> The script should work with any other source that supports **HTTPS**.

## Docker

```
docker run --rm \
--env-file=.env \
-v ${PWD}/repos.json:/git-backup-s3/repos.json \
pirobtumen/git-backup-s3
```

> Files .env and repos.json are required. Check the Configuration section.

## Configuration

Fill your environment variables inside the `.env` file:

```
GIT_USER=
GIT_TOKEN=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=
AWS_REGION=
```

Create the `repos.json` file:

```
[
    "github.com/<user>/<repo>.git",
    "github.com/<user>/<repo>.git",
    "gitlab.com/<user>/<repo>.git",
    "gitlab.com/<user>/<repo>.git",
    ...
]
```

## Resources

- [Gitlab create Oauth token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).
- [Create AWS S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html).

## Local development

> Requires Docker installed.

```
$ make run
```
