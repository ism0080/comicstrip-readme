"""
Comic Strip ReadMe
"""

import re
import os
import base64
import sys
import requests
from github import Github, GithubException

START_COMMENT = "<!--START_SECTION:comicstrip-->"
END_COMMENT = "<!--END_SECTION:comicstrip-->"
listReg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"

ghtoken = os.getenv("INPUT_GH_TOKEN")
repository = os.getenv("INPUT_REPOSITORY")
commit_message = os.getenv("INPUT_COMMIT_MESSAGE")
dilbert = os.getenv("INPUT_SHOW_DILBERT")
xkcd = os.getenv("INPUT_SHOW_XKCD")


def get_xkcd():
    pass


def get_dilbert():
    pass


def build_comicstrip():
    pass


def decode_readme():
    pass


def build_readme():
    pass


if __name__ == '__main__':
    pass
