#import moto
import boto3
#from moto import mock_rds2
import pprint

pp = pprint

rdsclient = boto3.client('rds', region_name='us-east-1')

#@mock_rds2



class RDSDisplayInstances(object):

    def disp_all_instances(self):
        desc_response = rdsclient.describe_db_instances()
        return desc_response


samakka = RDSDisplayInstances()

pp.pprint(samakka.disp_all_instances())
