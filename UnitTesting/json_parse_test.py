from __future__ import absolute_import, division, print_function
import boto3
from moto import mock_rds2
import pprint
import json

pp = pprint

rdsclient = boto3.client('rds', region_name='us-east-1')

@mock_rds2
class RDSSnapTest(object):

    def __init__(self, instance_name):
        self.instance_name = instance_name

    def crt_rds_inst(self):

        response = rdsclient.create_db_instance(
            DBName='rampandu',
            DBInstanceIdentifier=self.instance_name,
            AllocatedStorage=8,
            DBInstanceClass='db.t2.small',
            Engine='postgres',
            MasterUsername='jkpendyala',
            MasterUserPassword='iyyalna'
        )

        return response


    def chk_instance(self):
        runcrt = RDSSnapTest(self.instance_name)
        runcrt.crt_rds_inst()
        desc_response = rdsclient.describe_db_instances(DBInstanceIdentifier=self.instance_name)
        return desc_response


syera = RDSSnapTest('akru')
resp_obj = syera.chk_instance()
for k,v in resp_obj.items():
    if k=='DBInstances':
        for k1 in resp_obj['DBInstances'][0]:
            print(k1, " : ", end="")
            print(resp_obj['DBInstances'][0][k1])
            print("DBInstanceClass is : ", end="")

        #   code to print individually

        #   print(resp_obj['DBInstances'][0]['DBInstanceClass'])
        #   print("DBInstanceIdentifier is : ", end="")
        #   print(resp_obj['DBInstances'][0]['DBInstanceIdentifier'])
        #   print("DBInstanceStatus is : ", end="")
        #   print(resp_obj['DBInstances'][0]['DBInstanceStatus'])
        #   print("DBName is : ", end="")
        #   print(resp_obj['DBInstances'][0]['DBName'])