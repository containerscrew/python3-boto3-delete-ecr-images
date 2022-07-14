# Credentials

Credentials will be taken from your AWS_PROFILE in your terminal when you execute this python script.

```sh
aws configure
export AWS_PROFILE="myprofile" # will be set in the terminal where you'll execute the python script
```

# Example

```sh
ecr-lifecycle -a 90 -r eu-west-1 -n lifullconnect/platform/ads-ingester -d true
```

## Parameters

* **-a:** max age of the snapshot (default: 30 days)
* **-r:** aws region
* **-i:** aws account id
* **-l:** level info (default INFO)
* **-d:** dry run, only prints what happens, not execute
