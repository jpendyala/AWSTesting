import boto3
client = boto3.client('cloudformation', region_name='us-east-1')
response = client.create_stack(
    StackName='create-s3-bucket',
    TemplateURL='https://s3.amazonaws.com/my-jpendyala-bucket/create-s3-bucket.yml',
)
print (response)

