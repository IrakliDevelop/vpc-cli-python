import logging
from botocore.exceptions import ClientError

def create_igw(client):
    try:
        igw = client.create_internet_gateway()
        igw_id = igw['InternetGateway']['InternetGatewayId']
        logging.info(f"Created internet gateway {igw_id}")
        return igw_id
    except ClientError as e:
        logging.error(f"Error creating internet gateway: {e}")
        return None

def attach_igw_to_vpc(client, vpc_id, igw_id):
    try:
        client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        logging.info(f"Attached internet gateway {igw_id} to VPC {vpc_id}")
    except ClientError as e:
        logging.error(f"Error attaching internet gateway {igw_id} to VPC {vpc_id}: {e}")
        return False
    return True