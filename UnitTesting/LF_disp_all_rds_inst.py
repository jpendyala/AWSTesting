from disp_rds_inst_func import RDSDisplayInstances
#import moto
import boto3
#from moto import mock_rds2
import pprint

pp = pprint

def lambda_handler(event, context):
    disp = RDSDisplayInstances()
    awe = disp.disp_all_instances()



