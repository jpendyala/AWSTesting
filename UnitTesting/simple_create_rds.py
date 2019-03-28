import moto
import boto3
from moto import mock_rds2
import pprint

import random, string


pp = pprint

rdsclient = boto3.client('rds', region_name='us-east-1')

@mock_rds2

class RDSSnapTest:


    def gen_random_string(self):
        letters = string.ascii_lowercase
        rampandu = ''.join(random.choice(letters) for i in range(6))
        return rampandu

    def crt_rds_inst(self):

        random_string_class = RDSSnapTest()

        engine_type = ['postgres', 'mysql']


        for e_type in engine_type:

            random_string = random_string_class.gen_random_string()

            response = rdsclient.create_db_instance(
                DBName='rampandu',
                DBInstanceIdentifier=str(e_type) + str(random_string) + 'jaya',
                AllocatedStorage=8,
                DBInstanceClass='db.t2.small',
                Engine=e_type,
                MasterUsername='jkpendyala',
                MasterUserPassword='iyyalna',

            )
            pp.pprint(response)


jill=RDSSnapTest()
jill.crt_rds_inst()