# ECR lifecycle

Delete old images inside ECR repository using python and boto3

![python-logo](./img/python-logo.png)

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
