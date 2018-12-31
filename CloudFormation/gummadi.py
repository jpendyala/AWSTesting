import boto3
import pprint

pp=pprint

client = boto3.client('s3')
response = client.list_buckets()
pp.pprint(response)


