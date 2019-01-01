#!/usr/bin/python
import boto3
import argparse

# client = boto3.client('cloudformation', region_name='us-east-1')
# response = client.create_stack(
#     StackName='create-s3-bucket',
#     TemplateURL='https://s3.amazonaws.com/my-jpendyala-bucket/create-s3-bucket.yml',
# )
# print (response)


def cp_cf_template(stack_name, bucket_name):
    template_file = stack_name + '.yml'
    key = template_file
    response = s3_client.put_object(Body=template_file,
                                    Bucket=bucket_name,
                                    Key=key)


def mystack_create(stack_name, bucket_name):
    #client = boto3.client('cloudformation', region_name=region)

    response = cf_client.create_stack(
        StackName=stack_name,
        TemplateURL='https://s3.amazonaws.com/' + bucket_name + '/' + stack_name + '.yml'
    )
    print (response)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stack_name')
    parser.add_argument('--bucket_name')
    #parser.add_argument('--url')
    args = parser.parse_args()
    return args


def main(args):
    cp_cftemplate = cp_cf_template(args.stack_name, args.bucket_name)
    crt_stack = mystack_create(args.stack_name, args.bucket_name)


if __name__== "__main__":
    PARSED_ARGS = parse_arguments()
    #region_name = PARSED_ARGS.region_name
    cf_client = boto3.client('cloudformation', region_name='us-east-1')
    s3_client = boto3.client('s3', region_name='us-east-1')
    main(PARSED_ARGS)

# python createupdatestack.py --region_name 'us-east-1' --stack_name create-s3-bucket --url 'https://s3.amazonaws.com/my-jpendyala-bucket/create-s3-bucket.yml'



