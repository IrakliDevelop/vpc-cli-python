import logging
from botocore.exceptions import ClientError
def create_vpc(client, vpc_name):
    try:
        vpc = client.create_vpc(CidrBlock='10.0.0.0/16')
        vpc_id = vpc['Vpc']['VpcId']
        client.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": vpc_name}])
        logging.info(f"Created VPC {vpc_id} with name {vpc_name}")
        return vpc_id
    except ClientError as e:
        logging.error(f"Error creating VPC {vpc_name}: {e}")
        return None