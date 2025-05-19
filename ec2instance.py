#!/usr/bin/python3

import boto3

# Connect to EC2 service in the specified region
ec2 = boto3.resource('ec2', region_name='us-east-1')

# Requests the instance ID from the user
instance_id = input("Enter your EC2 instance ID (e.g. i-0abcd1234efgh5678): ")

# Retrieve and launch an instance object
try:
    instance = ec2.Instance(instance_id)
    response = instance.start()
    print("Instance starting...")
except Exception as e:
    print(f"Error: {e}")

# pip3 install boto3
# snap install aws-cli --classic
# aws configure
