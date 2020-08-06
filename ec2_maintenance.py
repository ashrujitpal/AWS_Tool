import boto3
import pprint
from aws.ec2.lifecycle_ec2 import EC2lifecycle

USER_CHOICE = '''
- Enter 'start' to start the EC2 instance(s)
- Enter 'stop' to stop the EC2 instance(s)
- Enter 'terminate' to terminate the EC2 instances(s)
- Enter 'reboot' to reboot the EC2 instance(s)
- Enter 'list' to list the EC2 instances-state wise
- Enter "g" to remove unattached volumes
- Enter "h" to create snapshots of an EC2 instance
- Enter "i" to prune old snapshots ("n") days old
- Enter 'j" to create an AMI from an existing EC2 instance
- Enter 'q' to quite from the current menu
'''
selection = input(USER_CHOICE)

while selection != 'q':

    if selection in 'start':
        EC2lifecycle.start_instances()
    elif selection in 'stop':
        EC2lifecycle.stop_instances()
    elif selection in 'terminate':
        EC2lifecycle.terminate_instances()
    elif selection in 'reboot':
        EC2lifecycle.reboot_instances()
    elif selection in 'list':
        EC2lifecycle.list_instances()
    elif selection in 'h':
        EC2lifecycle.create_snapshot()
    else:
        print('Unknown command. Please try again.')

    selection = input(USER_CHOICE)





