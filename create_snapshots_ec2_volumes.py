from datetime import datetime

import boto3

mgmt_console = boto3.session.Session(profile_name='administrator')
ec2_client = mgmt_console.client(service_name='ec2')

instances = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'bootstrap',
            ]
        }
    ]
)

reservations = instances['Reservations']

for reservation in reservations:
    local_instances = reservation['Instances']

    for instance in local_instances:

        print(instance)
        block_device_mappings = instance['BlockDeviceMappings']
        for block_device_mapping in block_device_mappings:
            volume = block_device_mapping['Ebs']
            volume_id = block_device_mapping['Ebs']['VolumeId']
            instance_id = instance['InstanceId']
            print(volume_id)
            print(instance_id)

            timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
            desc = 'Backup of {0}, volume {1}, created {2}'.format(instance_id, volume_id, timestamp)
            print(desc)

            snapshot = (Description=desc)
            print("Created Snapshot", snapshot.id)

