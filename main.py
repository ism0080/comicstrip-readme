"""
Comic Strip ReadMe
"""

import re
import os
import base64
import sys
import requests
from github import Github, GithubException
from bs4 import BeautifulSoup
from datetime import datetime

START_COMMENT = "<!--START_SECTION:comicstrip-->"
END_COMMENT = "<!--END_SECTION:comicstrip-->"
listReg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

ghtoken = os.getenv("INPUT_GH_TOKEN")
repository = os.getenv("INPUT_REPOSITORY")
commit_message = os.getenv("INPUT_COMMIT_MESSAGE")
xkcd = os.getenv("INPUT_SHOW_XKCD")
dilbert = os.getenv("INPUT_SHOW_DILBERT")


def get_xkcd() -> str:
    """Get image url for comic"""
    if xkcd == 'true':
        r = requests.get("https://xkcd.com/info.0.json").json()
        img = r['img']

        return f'<a href="https://xkcd.com/">\n <img src="{img}" />\n</a>'

    return ""


def get_dilbert() -> str:
    """Get image url for comic"""
    if dilbert == 'true':
        date = get_date()
        r = requests.get(f"https://dilbert.com/strip/{date}")
        s = BeautifulSoup(r.text, "html.parser")
        tag = s.find("meta", attrs={"property": "og:image"})
        img = tag.attrs['content']

        return f'<a href="https://dilbert.com/strip/{date}">\n <img src="{img}" />\n</a>'

    return ""


def get_date() -> str:
    """Get today's date in format YYYY/MM/DD"""
    return datetime.today().strftime('%Y-%m-%d')


def build_comicstrip() -> str:
    comicstrip = ""
    dilbert_comic = get_dilbert()
    xkcd_comic = get_xkcd()
    if dilbert_comic and xkcd_comic:
        comicstrip = f'<p align="center">\n {dilbert_comic}\n {xkcd_comic}\n</p>'
    if dilbert_comic and not xkcd_comic:
        comicstrip = f'<p align="center">\n {dilbert_comic}\n</p>'
    if xkcd_comic and not dilbert_comic:
        comicstrip = f'<p align="center">\n {xkcd_comic}\n</p>'
    if not (dilbert_comic or xkcd_comic):
        return comicstrip

    return comicstrip


def decode_readme(data: str) -> str:
    """Decode the contents of old readme"""
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')


def build_readme(comic: str, readme: str) -> str:
    """Generate a new README.md"""
    img = f"{START_COMMENT}\n{comic}\n{END_COMMENT}"
    return re.sub(listReg, img, readme)


if __name__ == '__main__':
    token = Github(ghtoken)
    try:
        repo = token.get_repo(repository)
    except GithubException:
        print("Authentication Error")
        sys.exit(1)
    file = repo.get_readme()
    comic = build_comicstrip()
    decoded_file = decode_readme(file.content)
    updated_readme = build_readme(comic=comic, readme=decoded_file)
    if updated_readme != decoded_file:
        repo.update_file(path=file.path, message=commit_message,
                         content=updated_readme, sha=file.sha, branch=repo.default_branch)
