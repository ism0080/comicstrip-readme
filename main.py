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
dilbert = os.getenv("INPUT_SHOW_DILBERT")
xkcd = os.getenv("INPUT_SHOW_XKCD")


def get_xkcd() -> str:
    """Get image url for comic"""
    if xkcd == 'true':
        r = requests.get("https://xkcd.com/info.0.json").json()

        return r['img']

    return ""


def get_dilbert() -> str:
    """Get image url for comic"""
    if dilbert == 'true':
        date = get_date()
        r = requests.get(f"https://dilbert.com/strip/{date}")
        s = BeautifulSoup(r.text, "html.parser")
        tag = s.find("meta", attrs={"property": "og:image"})

        return tag.attrs['content']

    return ""


def get_date():
    """Get today's date in format YYYY/MM/DD"""
    return datetime.today().strftime('%Y-%m-%d')


def build_comicstrip():
    pass


def decode_readme():
    pass


def build_readme():
    pass


if __name__ == '__main__':
    pass
