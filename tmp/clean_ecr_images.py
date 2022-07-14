import boto3
import time
from datetime import datetime, timedelta

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.list_images

current_time = datetime.now()


# def days_old(date):
#     date_obj = date.replace(tzinfo=None)
#     diff = datetime.datetime.now() - date_obj
#     return diff.days

images_to_delete = []


def delete_images(client, digest):
    print(f"Deleting {digest}")
    client.batch_delete_image(
        repositoryName='lifullconnect/platform/ads-ingester',
        imageIds=[
            {
                'imageDigest': digest,
            },
        ]
    )


def get_images(images):
    for image in images['imageDetails']:
        create_date = image['imagePushedAt']
        digest = image['imageDigest']

        day1 = create_date.strftime('%Y/%m/%d')
        day2 = current_time.strftime('%Y/%m/%d')

        d1 = datetime.strptime(day1, "%Y/%m/%d")
        d2 = datetime.strptime(day2, "%Y/%m/%d")

        delta = d2 - d1
        if delta.days > 90:
            images_to_delete.append(digest)

    print(f"We are going to delete {len(images_to_delete)} images")


def main():
    client = boto3.client('ecr', region_name="eu-west-1")
    images = client.describe_images(
        repositoryName='lifullconnect/platform/ads-ingester',
        maxResults=1000,
    )
    # print(images)
    #pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(images)
    get_images(images)
    
    # for digest in images_to_delete:
    #     delete_images(client, digest)
    

    # response = client.list_images(
    #     #registryId='string',
    #     repositoryName='lifullconnect/platform/ads-ingester',
    #     maxResults=2,
    # )
if __name__ == "__main__":
    main()
