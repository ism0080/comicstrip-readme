# Comic Strip

This GitHub Workflow updates your readme with the provided comic strips daily. The current comics available are:

-   [Dilbert](https://dilbert.com/)
-   [XKCD](https://xkcd.com/)

## Update your README

Add a comment to your `README.md`:

```md
<!--START_SECTION:comicstrip-->
<!--END_SECTION:comicstrip-->
```

The images will appear between the comments

### Profile Repository

_If you're executing the workflow on your Profile Repository (`<username>/<username>`)_

> You wouldn't need an GitHub Access Token since GitHub Actions already makes one for you.

Follow the bellow steps:

1. Go to your `<username>/<username>/actions`, hit `New workflow`, `set up a workflow yourself`, delete all the default content github made for you.
2. Copy the following code and paste it to your new workflow you created at step 1:

```yml
name: Comic Strip Readme

on:
    workflow_dispatch:
    schedule:
        # Runs at 8am UTC
        - cron: "0 8 * * *"

jobs:
    update-readme:
        name: Update README with Comic Strip
        runs-on: ubuntu-latest
        steps:
            - uses: ism0080/comicstrip-readme@master
              with:
                  SHOW_DILBERT: true
                  SHOW_XKCD: true
```

This will add the Dilbert and XKCD comics to your `README.md` at 8am UTC everyday

3. Add a comment to your `README.md` like this:

```md
<!--START_SECTION:comicstrip-->
<!--END_SECTION:comicstrip-->
```

4. Go to Workflows menu (mentioned in step 1), click `Comic Strip Readme`, click `Run workflow`.

5. Go to your profile page. you will be able to see it.

### Other Repository (not Profile)

_If you're executing the workflow on another repo other than `<username>/<username>`_

You'll need to get a [GitHub Access Token](https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token) with a `repo` scope and save it in the Repo Secrets `GH_TOKEN = <Your GitHub Access Token>`

Here is Sample Workflow File for running it:

```yml
name: Comic Strip Readme

on:
    schedule:
        # Runs at 12am UTC
        - cron: "0 8 * * *"

jobs:
    update-readme:
        name: Update README with Comic Strip
        runs-on: ubuntu-latest
        steps:
            - uses: ism0080/comicstrip-readme@master
              with:
                  SHOW_DILBERT: true
                  SHOW_XKCD: true
                  GH_TOKEN: ${{ secrets.GH_TOKEN }}
                  REPOSITORY: <username/username> # optional, By default, it will automatically use the repository who's executing the workflow.
```

### Extras

1. You can specify a commit message to override the default _"Updated readme comic strip"_. Add `COMMIT_MESSAGE` with the commit message you want

```yml
with:
    COMMIT_MESSAGE: Readme updated
```

2. If you only want one of the comics, just simply remove the variable from the `with` statement

_*Sometimes the comic may not be updated daily*_
