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


        engine_type = ['postgres', 'mysql', 'oracle-se']



        for e_type in engine_type:


            e_type_len = len(e_type)
            counter = 1
            while counter < e_type_len:
                random_string = random_string_class.gen_random_string()
                print("random string:", random_string)


                try:

                    rdsclient.create_db_instance(
                        DBName='rampandu',
                        DBInstanceIdentifier=random_string + str(counter),
                        AllocatedStorage=8,
                        DBInstanceClass='db.t2.small',
                        Engine=e_type,
                        MasterUsername='jkpendyala',
                        MasterUserPassword='iyyalna',
                        PubliclyAccessible=True

                    )

                except Exception as e:
                    print("Exception:", e)




                counter = counter + 1