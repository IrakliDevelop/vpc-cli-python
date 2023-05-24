import logging
from botocore.exceptions import ClientError
def launch_ec2_instance(client, subnet_id, security_group_id, key_pair_name):
    try:
        instance = client.run_instances(
            ImageId='ami-0abcdef1234567890',  # replace this with the correct AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName=key_pair_name,
            NetworkInterfaces=[
                {
                    'SubnetId': subnet_id,
                    'DeviceIndex': 0,
                    'AssociatePublicIpAddress': True,
                    'Groups': [security_group_id]
                }
            ],
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'VolumeSize': 10,
                        'VolumeType': 'gp1'
                    }
                }
            ]
        )
        instance_id = instance['Instances'][0]['InstanceId']
        return instance_id
    except Exception as e:
        logging.error(f"Could not launch EC2 instance: {e}")
        return None