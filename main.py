import git
import os
import json

GIT_TOKEN = os.getenv("GIT_TOKEN")
GIT_USER = os.getenv("GIT_USER")
REPOS_JSON = "repos.json"


def get_repos():
    repos = []

    with open(REPOS_JSON) as json_file:
        repos = json.load(json_file)
        
    return repos


def clone_and_zip(repo_url, repo_path, repo_zip):
    repo = git.Repo.clone_from(
        repo_url,
        to_path=repo_path,
        multi_options=["-c http.sslVerify=false"])

    with open(repo_zip, "wb") as zipfile:
        repo.archive(zipfile, format='zip')


def upload_to_s3(repo_zip):
    pass


def main():
    repos = get_repos()

    for repo in repos:
        repo_url = f'https://{GIT_USER}:{GIT_TOKEN}@{repo}'
        repo_name = repo_url.split("@")[1][:-4].replace("/", "_")
        repo_path = f"./backups/{repo_name}"
        repo_zip = f"{repo_path}.zip"

        print(f"\nCloning: {repo_name}")
        if (os.path.isdir(repo_path)):
            print("-> Repo already exists. Skipping.")
        else:
            clone_and_zip(repo_url, repo_path, repo_zip)
            print("-> OK")

        print(f"Uploading: {repo_zip}")
        upload_to_s3(repo_zip)
    
    print("FINITO")


if __name__ == "__main__":
    main()
