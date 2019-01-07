import moto
import boto3
from moto import mock_ec2
import pprint

import random, string


pp = pprint

ec2client = boto3.client('ec2', region_name='us-east-1')

@mock_ec2

class Create_Subnet_Test:


    def create_vpc(self):
        vpc = ec2client.create_vpc(CidrBlock='192.168.0.0/16')
        myVPC = (vpc['Vpc']['VpcId'])
        return myVPC



    def create_ec2_subnet(self):
        vp = Create_Subnet_Test()
        myVPCID = vp.create_vpc()

        subnet1 = ec2client.create_subnet(AvailabilityZone='us-east-1a', CidrBlock='192.168.1.0/24', VpcId=myVPCID)
        subnet2 = ec2client.create_subnet(AvailabilityZone='us-east-1c',CidrBlock='192.168.64.0/24', VpcId=myVPCID)
        mySubnet1 = subnet1['Subnet']['SubnetId']
        mySubnet2 = subnet2['Subnet']['SubnetId']
        return (mySubnet1, mySubnet2)


ulfa = Create_Subnet_Test()
pulli = ulfa.create_ec2_subnet()