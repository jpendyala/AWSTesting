import moto
import boto3
from moto import mock_rds2
import pprint
from create_subnet_test import *

import random, string


pp = pprint

rdsclient = boto3.client('rds', region_name='us-east-1')

@mock_rds2

class RDSSnapTest:


    def gen_random_string(self):
        letters = string.ascii_lowercase
        rampandu = ''.join(random.choice(letters) for i in range(6))
        return rampandu


    def create_rds_subnet_grp(self):
        mock = Create_Subnet_Test()
        (mysubnet1, mysubnet2) = mock.create_ec2_subnet()
        dbsubnet = rdsclient.create_db_subnet_group(
            DBSubnetGroupName='MyDBSubnetGroup',
            DBSubnetGroupDescription='MyDBSubnetGroup',
            SubnetIds=[mysubnet1, mysubnet2]
        )
        dbsubnet_grp_name = dbsubnet['DBSubnetGroup']['DBSubnetGroupName']
        return dbsubnet_grp_name


    def crt_rds_inst(self):

        random_string_class = RDSSnapTest()
        subnet_grp = str(random_string_class.create_rds_subnet_grp())


        engine_type = ['postgres', 'mysql', 'oracle-se']


        for e_type in engine_type:


            e_type_len = len(e_type)
            counter = 1
            while counter < e_type_len:
                random_string = random_string_class.gen_random_string()
               # print("random string:", random_string)

                if counter % 2 == 0:
                    public_access = True
                    multi_az = True

                else:
                    public_access = False
                    multi_az = True


                try:

                    rdsclient.create_db_instance(
                        DBName='rampandu',
                        DBInstanceIdentifier=random_string + str(counter),
                        AllocatedStorage=8,
                        DBInstanceClass='db.t2.small',
                        Engine=e_type,
                        MasterUsername='jkpendyala',
                        MasterUserPassword='iyyalna',
                        PubliclyAccessible=public_access,
                        MultiAZ=multi_az,
                        DBSubnetGroupName=subnet_grp

                    )

                except Exception as e:
                    print("Exception:", e)


                counter = counter + 1
