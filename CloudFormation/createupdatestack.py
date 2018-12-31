#!/usr/bin/python
import boto3
import argparse

# client = boto3.client('cloudformation', region_name='us-east-1')
# response = client.create_stack(
#     StackName='create-s3-bucket',
#     TemplateURL='https://s3.amazonaws.com/my-jpendyala-bucket/create-s3-bucket.yml',
# )
# print (response)


def mystack_create(region_name, stack_name, url):
    client = boto3.client('cloudformation', region_name=region_name)
    response = client.create_stack(
        StackName=stack_name,
        TemplateURL=url
    )
    print (response)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--region_name')
    parser.add_argument('--stack_name')
    parser.add_argument('--url')
    args = parser.parse_args()
    return args


def main(args):
    crt_stack = mystack_create(args.region_name, args.stack_name, args.url)


if __name__== "__main__":
    PARSED_ARGS = parse_arguments()
    main(PARSED_ARGS)

# python createupdatestack.py --region_name 'us-east-1' --stack_name create-s3-bucket --url 'https://s3.amazonaws.com/my-jpendyala-bucket/create-s3-bucket.yml'


