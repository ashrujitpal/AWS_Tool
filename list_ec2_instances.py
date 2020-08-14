import boto3
from datetime import datetime
import pprint

management_cons = boto3.session.Session(profile_name='administrator')

status = input('Please enter the status for which you want to delete the snapshots?')
region_name = input("Please enter the region name: ")


def delete_snapshots_by_ids(ec2_cli, snapshot_ids):
    for snapshot_id in snapshot_ids:
        # snapshot_id = f"'{snapshot_id}',"
        print(snapshot_id)
        try:
            response = ec2_cli.delete_snapshot(SnapshotId=snapshot_id)
            pp = pprint.PrettyPrinter(indent=4)
            print(f'Deleting the snapshot id: {snapshot_id}')
            pp.pprint(response)
        except Exception as exe:

            if 'InvalidSnapshot.InUse' in exe:
                print("Snapshot {} in use, skipping deletion".format(snapshot_id))
            else:
                print(exe)
            continue


try:
    ec2_cli = management_cons.client(service_name='ec2', region_name=region_name)
    account_id = management_cons.client(service_name='sts').get_caller_identity()['Account']

    snapshots = ec2_cli.describe_snapshots(
        Filters=[
            {
                'Name': 'owner-id',
                'Values': [account_id]
            }
        ])['Snapshots']

    new_snapshots = [snapshot for snapshot in snapshots if snapshot['status'] == status]
    snapshot_ids = [snapshot['SnapshotId'] for snapshot in new_snapshots]
    delete_snapshots_by_ids(ec2_cli, snapshot_ids)

except Exception as exe:
    print(exe)



