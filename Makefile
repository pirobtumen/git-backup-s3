.PHONY=run

IMAGE=git-backup-s3

build:
	docker build . --tag ${IMAGE}

# DEBUG
# -v ${PWD}/backups:/git-backup-s3/backups

run: build
	docker run \
	--rm \
	--env-file=.env \
	-v ${PWD}/repos.json:/git-backup-s3/repos.json \
	${IMAGE}
