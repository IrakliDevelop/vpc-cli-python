# AWS VPC CLI

This is a simple CLI that interacts with AWS to create a Virtual Private Cloud (VPC), gives it a name, creates an Internet Gateway (IGW), and attaches the IGW to the VPC.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6+
- You have installed [Poetry](https://python-poetry.org/)
- You have an AWS account with access to create and manage VPC and IGW resources.
- You have your AWS credentials (AWS Access Key ID and AWS Secret Access Key) and region configured in a .env file.

## Installing AWS VPC CLI

To install AWS VPC CLI, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/IrakliDevelop/vpc-cli-python
cd vpc-cli-python
```

2. Install the dependencies using Poetry:

```bash
poetry install
```

3. Create a `.env` file in the project directory with your AWS credentials:

```bash
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=your_aws_region
```

Replace `your_access_key_id`, `your_secret_access_key`, and `your_aws_region` with your actual AWS credentials and region.

## Using AWS VPC CLI

To use AWS VPC CLI, run the following command:

```bash
poetry run python main.py <vpc_name>
```

Replace `<vpc_name>` with the name you want to assign to the VPC. This script will create a VPC with the specified name, create an IGW, and attach the IGW to the VPC. It will then print the IDs of the created VPC and IGW.

## Contributing to AWS VPC CLI

To contribute to AWS VPC CLI, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin aws_vpc_cli/<branch_name>`
5. Create the pull request.

## License

This project uses the following license: [MIT License](https://opensource.org/license/mit/).
