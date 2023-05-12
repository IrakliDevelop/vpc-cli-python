import argparse

from utils.create_vpc import create_vpc
from utils.igw import create_igw, attach_igw_to_vpc
from utils.init_client import init_client
def main():
    parser = argparse.ArgumentParser(description="AWS VPC and IGW CLI")
    parser.add_argument("vpc_name", help="Name of the VPC to be created")
    args = parser.parse_args()

    client = init_client()

    vpc_id = create_vpc(client, args.vpc_name)

    igw_id = create_igw(client)

    attach_igw_to_vpc(client, vpc_id, igw_id)

if __name__ == "__main__":
    main()