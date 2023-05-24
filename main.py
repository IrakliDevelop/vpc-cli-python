import argparse

from utils.create_vpc import create_vpc
from utils.ec2_instance import launch_ec2_instance
from utils.igw import create_igw, attach_igw_to_vpc
from utils.init_client import init_client
from utils.key_pair import create_key_pair
from utils.security_group import create_security_group, add_security_group_rules

def main():
    parser = argparse.ArgumentParser(description="AWS VPC and IGW CLI")
    parser.add_argument("vpc_name", help="Name of the VPC to be created")
    parser.add_argument("vpc_id", help="ID of the VPC")
    parser.add_argument("subnet_id", help="ID of the Subnet")
    args = parser.parse_args()

    client = init_client()

    if args.vpc_name:
        vpc_id = create_vpc(client, args.vpc_name)

        igw_id = create_igw(client)
        attach_igw_to_vpc(client, vpc_id, igw_id)
    elif args.vpc_id and args.subnet_id:
        security_group_id = create_security_group(client, args.vpc_id)
        add_security_group_rules(client, security_group_id)

        key_pair = create_key_pair(client)
        with open("EC2-Key-Pair.pem", "w") as key_file:
            key_file.write(key_pair)

        instance_id = launch_ec2_instance(client, args.subnet_id, security_group_id, "EC2-Key-Pair")
        print(f"Launched EC2 instance with ID {instance_id}")
    else:
        print("Please provide either a VPC name or a VPC ID and subnet ID")

if __name__ == "__main__":
    main()