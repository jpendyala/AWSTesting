#import moto
import boto3
#from moto import mock_rds2
import pprint


pp = pprint

lamdba_clnt = boto3.client('lambda','us-east-1')

#@mock_lambda

class LambdaCreateTest:

    def create_lambda_test(self):

        response = lamdba_clnt.create_function(
            FunctionName='myRDSTestLambda',
            Runtime='python3.6',
            Role='arn:aws:iam::030703475290:role/lambda_basic_execution',
            Handler='LF_disp_all_rds_inst.lambda_handler',
            Code={

                'S3Bucket': 'pendyala4-bucket',
                'S3Key': 'Archive.zip'

            },
            Description='string',
            Timeout=10,
            MemorySize=128,
            Publish=False
        )