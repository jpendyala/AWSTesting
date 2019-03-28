#import moto
import boto3
#from moto import mock_rds2
import pprint
from create_simple_lambda import LambdaCreateTest


pp = pprint

lamdba_clnt = boto3.client('lambda','us-east-1')

#@mock_lambda

class InvokeLambdaTest:

    def invoke_lambda_test(self):

        lct = LambdaCreateTest()
        csl = lct.create_lambda_test()

        response = lamdba_clnt.invoke(
            FunctionName='myRDSTestLambda',
            InvocationType='RequestResponse',
            LogType='Tail',
        )
        return response


gtest = InvokeLambdaTest()
pp.pprint(gtest.invoke_lambda_test() )






