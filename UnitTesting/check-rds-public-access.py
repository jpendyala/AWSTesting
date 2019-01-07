from __future__ import absolute_import, division, print_function
from disp_all_rds_inst import RDSDisplayInstances
import moto
import boto3
from moto import mock_rds2
import pprint

pp = pprint

rdsclient = boto3.client('rds', region_name='us-east-1')

@mock_rds2

class CheckRDSPublicAccess(object):

    def rds_audit_checks(self):
        upma = RDSDisplayInstances()
        chutney = upma.disp_all_instances()
        return chutney


tillu = CheckRDSPublicAccess()
ramesh = tillu.rds_audit_checks()

print("RDS Instance with Publicly Accessible: True: ")
print("============================================= ")
for k,v in ramesh.items():
    i = 0
    if k == 'DBInstances':
        for k1 in ramesh['DBInstances']:
            # print(k1, " : ", end="")
            # Do no Delete below statement
            # print(ramesh['DBInstances'][i]['Engine'] + ',' + ramesh['DBInstances'][i]['DBInstanceIdentifier'] + ',' + str(ramesh['DBInstances'][i]['PubliclyAccessible']) )
            public_access = str(ramesh['DBInstances'][i]['PubliclyAccessible'])

            if public_access == 'True':
                print('DB Instance Engine: ' + ramesh['DBInstances'][i]['Engine'] + ', DB Instance ID: ' + ramesh['DBInstances'][i]['DBInstanceIdentifier'] + ', Original Value: ' + str(ramesh['DBInstances'][i]['PubliclyAccessible'] ) )

            i = i+1


