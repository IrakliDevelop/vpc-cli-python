import logging
from botocore.exceptions import ClientError

def create_key_pair(client):
    try:
        key_pair = client.create_key_pair(KeyName='EC2-Key-Pair')
        return key_pair['KeyMaterial']
    except ClientError as e:
        logging.error(f"Could not create key pair: {e}")
        return None