# Pre-commit

`pre-commit` is a framework for managing and maintaining multi-language
pre-commit hooks. You may refer to its website [pre-commit](www.pre-commit.com)
for detailed info.

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

## Installation

```shell
$ pip install pre-commit
$ pre-commit --version
pre-commit 3.0.4
```

## Quick Start

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

## Adding pre-commit plugins to your project

The `.pre-commit-config.yaml` file describes what repositories and hooks are
installed.

### .pre-commit-config.yaml - top level

|keywords       |    Description       |
|:-------------:|:--------------------:|
|repos          |A list of repository mappings|
|files          |(optional:default`''`) global file include pattern|
|exclude        |(optional:default`^$`) global file exclude pattern|
|fail_fast      |(optional:default`false`) set to `true` to have pre-commit stop running hooks after the first failure.|
|minimum_pre_commit_version|(optional:default`'0'`) require a minimu version of pre-commit.|

A sample top-level:
```shell
exclude: '^$'
fail_fast: false
repos:
  - ...
```

### .pre-commit-config.yaml - repos

|keywords       |    Description       |
|:-------------:|:--------------------:|
|repo           | the repository url to `git clone` from|
|rev            | the revision to tag to clone at|
|hooks          | A list of hook mappings|

A sample repository:
```shell
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
      - ...
```

### .pre-commit-config.yaml - hooks

|keywords       |    Description       |
|:-------------:|:--------------------:|
|id             |which hook from the repository to use.|
|alias          |(optional) allows to be referenced when using `pre-commit run <hookid>`|
|name           |(optional) name during hook execution|
|files          |(optional) override the default pattern for files to run on.|
|types          |(optional) override the default file types to run on (AND).|
|types_or       |(optional) override the default file types to run on (OR).|
|args           |(optional) list of additional parameters to pass to the hook.|\
|stages         |(optional) confines the hook to the `commit`, `merge-commit`, `push`, `prepare-commit-msg`, `commit-msg`, `post-checkout`, `post-commit`, `post-merge`, `post-rewrite`, or `manual` stage.|
|additional_dependencies|(optional) list of dependencies that need to be installed.|
|always_run     |(optional) if `true`, hook will run even if there are no matching files.|
|verbose        |(optional) if `true`, forces to print output of the hook even if the hook passes.|
|log_file       |(optional) hook output will be written to a file when the hook fails or verbose is `true`.|

an example of a complete configuration:

```shell
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
      - id: pip-compile
        args:
          - --allow-insafe
          - --extra=dev
          - --output-file=requirements-dev.txt
          - --quiet
          - --upgrade
          - pyproject.toml
        files: ^pyproject\.toml$
```

## Update hooks automatically

run `pre-commit autoupdate`, and this will bring the hooks to the latest tag on
default branch.
