# ECR lifecycle (Alpha)

Delete old images inside ECR repository using python and boto3

![python-logo](./img/python-logo.png)

[![Pylint](https://github.com/nanih98/python3-boto3-delete-ecr-images/actions/workflows/publish-to-test-pypi.yml/badge.svg)](https://github.com/nanih98/python3-boto3-delete-ecr-images/actions/workflows/publish-to-test-pypi.yml)


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [ECR lifecycle (Alpha)](#ecr-lifecycle-alpha)
- [Credentials](#credentials)
- [Installation](#installation)
- [Usage](#usage)
  - [Parameters](#parameters)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Credentials

Credentials will be taken from your AWS_PROFILE in your terminal when you execute this python script.

```sh
aws configure
export AWS_PROFILE="myprofile" # will be set in the terminal where you'll execute the python script
```

# Installation

This tool is available in pypip package, so you can install it using your command line:

```bash
$ pip3 install ecr-lifecycle
```

# Usage

```sh
ecr-lifecycle -a 90 -r eu-west-1 -n repository/test/repo_name -l INFO -d true
```

## Parameters

* **-a:** max age of the image(default: 30 days)
* **-r:** aws region
* **-n:** ECR repository name
* **-l:** level info (default INFO)
* **-d:** dry run, only prints what happens, not execute
