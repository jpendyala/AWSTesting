import moto
import boto3
from moto import mock_rds2
import pprint

pp = pprint

rdsclient = boto3.client('rds', region_name='us-east-1')

@mock_rds2

class RDSSnapTest:

    def __init__(self, instance_name):
        self.instance_name = instance_name

    def crt_rds_inst_postgres(self):

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


    def crt_rds_inst_mysql(self):

        response_rds = rdsclient.create_db_instance(
            DBName='pochalu',
            DBInstanceIdentifier=self.instance_name,
            AllocatedStorage=8,
            DBInstanceClass='db.t2.small',
            Engine='mysql',
            MasterUsername='tiger',
            MasterUserPassword='pulibabu1'
        )

        return response_rds


    def crt_rds_inst_oracle(self):

        response_rds = rdsclient.create_db_instance(
            DBName='pochalu-oracle',
            DBInstanceIdentifier=self.instance_name,
            AllocatedStorage=8,
            DBInstanceClass='db.t2.small',
            Engine='oracle-se',
            MasterUsername='tiger',
            MasterUserPassword='pulibabu1'
        )

        return response_rds



    def chk_instance(self):
        desc_response = rdsclient.describe_db_instances(DBInstanceIdentifier=self.instance_name)
        return desc_response

    def method_test(self):
        print ('this is a test in super class for instance: '+self.instance_name)




runcrt = RDSSnapTest('akrux')
pp.pprint(runcrt.crt_rds_inst_mysql())
pp.pprint(runcrt.crt_rds_inst_postgres())
pp.pprint(runcrt.crt_rds_inst_oracle())

