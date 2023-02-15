# Pre-commit

## Introduction

**Git hooks** are *shell scripts found in the hidden .git/hooks directory* of a
Git repository. These scripts trigger actions in response to the specific
events, so they can help you automate your development lifecycle. Although you
may never have noticed them, every Git repository includes 12 sample scripts.

**Pre-commit** runs the hooks on every commit to automatically point out issues
in code such as missing semicoluns, trailing whitespace, and debug statements.
By pointing these issues out before code review, this allows a code reviewer to
focus on the architecture of a change while not wasting time with trivial style
nitpicks.

# Installation

```shell
$ pip install pre-commit
$ pre-commit --version
pre-commit 3.0.4
```

# Quick Start

1. Add a pre-commit configuration

* create a file named `.pre-commit-config.yaml` (you can genereate a very basic
  configuration using `pre-comit sample-config`)

```shell
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
```

* you may refer to other [supported hooks](https://pre-commit.com/hooks.html).

2. Install the git hook scripts

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

now `pre-commit` will run automatically on `git commit`!

3. (optional) Run against all the files

By default `pre-commit` will only run on the changed files during git hooks, but
it could be a good idea to run the hooks against all of the files when adding
new hooks:

```shell
$ pre-commit run --all-files
```
