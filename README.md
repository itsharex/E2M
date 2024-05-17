# E2M (Everything to Markdown)

<p align="center">
    <a href="https://github.com/Jing-yilin/E2M">
        <img src="https://img.shields.io/badge/E2M-repo-blue" alt="E2M Repo">
    </a>
</p>

- [E2M (Everything to Markdown)](#e2m-everything-to-markdown)
  - [Introduction](#introduction)
  - [Install](#install)
  - [Get Started](#get-started)
    - [Quick Start](#quick-start)
    - [Set to Development Environment](#set-to-development-environment)
    - [Set to Production Environment](#set-to-production-environment)
  - [How to contribute](#how-to-contribute)
    - [Create a new branch](#create-a-new-branch)
    - [PEP8 style](#pep8-style)
    - [Push to the remote repository](#push-to-the-remote-repository)
    - [Pull Request](#pull-request)
  - [Supported File Types](#supported-file-types)
  - [Contributing](#contributing)
    - [Contributors](#contributors)

## Introduction

This project aims to provide an API, which can convert everything to markdown (LLM-friendly Format).

## Install

```bash
git clone https://github.com/Jing-yilin/E2M
cd E2M
conda create -n e2m python=3.10
conda activate e2m
python -m pip install -r requirements.txt
```

## Get Started

### Quick Start

```bash
# make sure you are in E2M/app
cd app
flask run --host 0.0.0.0 --port=8765
# you can add --debug to enable debug mode
```

### Set to Development Environment

```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
```

### Set to Production Environment

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
```

## How to contribute

### Create a new branch

Before you commit your code, please create a new branch:

-   `feature/xxx` for new features
-   `bugfix/xxx` for bug fixes

You can create a new branch with the following command:

```bash
# fetch the latest cod
git checkout main
git pull
# create a new branch
git checkout -b feature/xxx
```

### PEP8 style

Then, run the following commands to check the style of your code:

```bash
# all contributions should follow PEP8 style
flake8 .  # to check the style
black .  # to format the code
```

### Push to the remote repository

```bash
# add the changes
git add .
# commit the changes
git commit -m "your commit message"
# push the changes
git push origin feature/xxx # or simply `git push`
```

### Pull Request

```bash
# create a pull request on GitHub
```

## Supported File Types

## Contributing

### Contributors

<a href="https://github.com/Jing-yilin/E2M/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Jing-yilin/E2M" />
</a>
