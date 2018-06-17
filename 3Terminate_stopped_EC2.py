#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
ids = ['i-0f31b29a8752a52d0']
ec2.instances.filter(InstanceIds=ids).terminate()
