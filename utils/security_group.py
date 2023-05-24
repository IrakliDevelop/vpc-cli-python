import requests
import logging
from botocore.exceptions import ClientError

def create_security_group(client, vpc_id):
    try:
        response = client.create_security_group(GroupName='SSH-HTTP-Access', Description='Security group for SSH and HTTP access', VpcId=vpc_id)
        security_group_id = response['GroupId']
        return security_group_id
    except ClientError as e:
        logging.error(f"Could not create security group: {e}")
        return None

def add_security_group_rules(client, security_group_id):
    try:
        # Get the public IP of the current machine
        public_ip = requests.get('https://api.ipify.org').text + '/32'

        # Add inbound rules for HTTP and SSH access
        client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': public_ip}]}
            ]
        )
    except ClientError as e:
        logging.error(f"Could not add rules to security group: {e}")