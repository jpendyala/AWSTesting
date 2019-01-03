import moto
import boto3
from moto import mock_rds2
import pprint

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


    def crt_db_snapshot(self):
        crt_snp = RDSSnapTest(self.instance_name)
        crt_snp.crt_rds_inst()
        ret_snap = rdsclient.create_db_snapshot(DBSnapshotIdentifier='dbphoto', DBInstanceIdentifier=self.instance_name)
        return ret_snap


syera = RDSSnapTest('akru')
pp.pprint(syera.crt_db_snapshot())

















