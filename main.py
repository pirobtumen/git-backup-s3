import git
import os
import json
import boto3
import logging
from botocore.exceptions import ClientError
from datetime import datetime

GIT_TOKEN = os.getenv("GIT_TOKEN")
GIT_USER = os.getenv("GIT_USER")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")
BACKUP_FREQ = os.getenv("BACKUP_FREQ")
APPEND_DATE = os.getenv("APPEND_DATE") == "true"
REPOS_JSON = "repos.json"


def get_repos():
    repos = []

    with open(REPOS_JSON) as json_file:
        repos = json.load(json_file)
        
    return repos


def clone_and_zip(repo_url, repo_path, repo_zip_path):
    repo = git.Repo.clone_from(
        repo_url,
        to_path=repo_path)

    with open(repo_zip_path, "wb") as zipfile:
        repo.archive(zipfile, format='zip')


def upload_to_s3(repo_zip_path, repo_zip_name):
    s3 = boto3.client('s3', region_name=AWS_REGION)

    try:
        s3.upload_file(repo_zip_path, AWS_S3_BUCKET, repo_zip_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    repos = get_repos()

    for repo in repos:
        repo_url = f'https://{GIT_USER}:{GIT_TOKEN}@{repo}'
        repo_name = repo_url.split("@")[1].replace("/", "_")
        print(f"\nCloning: {repo_name}")

        if APPEND_DATE:
            # Get today's date to append to the backup folder name
            now = datetime.now()
            repo_name += f"_{now.strftime('%Y_%m_%d')}"

        repo_path = f"./backups/{repo_name}"
        repo_zip_name = f"{repo_name}.zip"
        repo_zip_path = f"{repo_path}.zip"

        if (os.path.isdir(repo_path)):
            print("-> Repo already exists. Skipping.")
        else:
            clone_and_zip(repo_url, repo_path, repo_zip_path)
            print("-> OK")

        print(f"Uploading: {repo_zip_name}")
        uploaded = upload_to_s3(repo_zip_path, repo_zip_name)
        if uploaded:
            print("-> OK")
        else:
            print("-> Error")
    
    print("FINITO")


if __name__ == "__main__":
    main()
