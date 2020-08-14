from datetime import datetime
import sys
import boto3
import botocore
import pprint

from dateutil.tz import tzutc

from aws.ec2.list_ec2_instances import ListEC2Instances
from datetime import datetime, timedelta

profile = 'administrator'

try:
    management_cons = boto3.session.Session(profile_name=profile)
except botocore.exceptions.ProfileNotFound:
    print(f'The config profile ({profile}) could not be found')
except Exception as e:
    print(e)
    sys.exit(1)


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


class EC2lifecycle:

    @staticmethod
    def stop_instances():
        try:
            ec2_ids = ListEC2Instances().display_ec2()

            if len(ec2_ids['instances_ids']) > 0:
                input_region_name = input(
                    "Please enter the corresponding region name if you want to stop all instances for a region")
                input_ec2_id = input(
                    "Please enter the instance id if you want to stop a particular instance in the above \n"
                    "specified region, to enter multiple instances, seperate them with comma")
                print(input_region_name)
                print(ec2_ids['regions'])
                if input_region_name in ec2_ids['regions']:
                    if input_ec2_id == 'all':
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        # Get only running instances
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-state-name',
                                      'Values': ['running']}])
                        # Start the instances
                        for instance in instances:
                            print(f'Stopping instance {instance.id}')
                            instance.stop()
                            instance.wait_until_stopped()
                            print('Stopped instance: ', instance.id)
                    elif len(input_ec2_id.strip('\n').split(',')) > 0:
                        input_ec2_ids = input_ec2_id.strip('\n').split(',')
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-id',
                                      'Values': input_ec2_id.strip('\n').strip(' ').split(',')}])
                        # Start the instances
                        for instance in instances:
                            print(f'Stopping instance {instance.id}')
                            instance.stop()
                            instance.wait_until_stopped()
                            print('Stopped instance: ', instance.id)
                else:
                    print('Exiting from the given tasks')
        except botocore.exceptions.NoRegionError:
            print(f'You have inputted an invalid region name ')
            sys.exit(2)
        except Exception as exe:
            print(exe)
            sys.exit(3)

    @staticmethod
    def terminate_instances():
        try:
            ec2_ids = ListEC2Instances().display_ec2()

            if len(ec2_ids['instances_ids']) > 0:
                input_region_name = input(
                    "Please enter the corresponding region name if you want to terminate all instances for a region")
                input_ec2_id = input(
                    "Please enter the instance id if you want to terminate a particular instance in the above \n"
                    "specified region, to enter multiple instances, seperate them with comma")
                print(input_region_name)
                print(ec2_ids['regions'])
                if input_region_name in ec2_ids['regions']:
                    if input_ec2_id == 'all':
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        # Get only running instances
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-state-name',
                                      'Values': ['running']}])
                        # Start the instances
                        for instance in instances:
                            print(f'Terminating instance {instance.id}')
                            instance.terminate()
                            instance.wait_until_terminated()
                            print('Terminated instance: ', instance.id)
                    elif len(input_ec2_id.strip('\n').split(',')) > 0:
                        input_ec2_ids = input_ec2_id.strip('\n').split(',')
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-id',
                                      'Values': input_ec2_id.strip('\n').strip(' ').split(',')}])
                        # Start the instances
                        for instance in instances:
                            print(f'Terminating instance {instance.id}')
                            instance.terminate()
                            instance.wait_until_terminated()
                            print('Terminated instance: ', instance.id)
                else:
                    print('Exiting from the given tasks')
        except botocore.exceptions.NoRegionError:
            print(f'You have inputted an invalid region name ')
            sys.exit(2)
        except Exception as exe:
            print(exe)
            sys.exit(3)

    @staticmethod
    def reboot_instances():
        try:
            ec2_ids = ListEC2Instances().display_ec2()

            if len(ec2_ids['instances_ids']) > 0:
                input_region_name = input(
                    "Please enter the corresponding region name if you want to reboot all instances for a region")
                input_ec2_id = input(
                    "Please enter the instance id if you want to reboot a particular instance in the above \n"
                    "specified region, to enter multiple instances, seperate them with comma")
                if input_region_name in ec2_ids['regions']:
                    if input_ec2_id == 'all':
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        # Get only running instances
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-state-name',
                                      'Values': ['pending', 'running']}])
                        # Start the instances
                        print("Instasncs with the status 'running' and 'pending' are only rebooting:::")
                        for instance in instances:
                            print(f'Rebooting instance {instance.id}')
                            instance.reboot()

                            print('Rebooted instance: ', instance.id)
                    elif len(input_ec2_id.strip('\n').split(',')) > 0:
                        input_ec2_ids = input_ec2_id.strip('\n').split(',')
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-id',
                                      'Values': input_ec2_id.strip('\n').strip(' ').split(',')}])
                        # Start the instances
                        for instance in instances:
                            print(f'Rebooting instance {instance.id}')
                            instance.reboot()

                            print('Rebooted instance: ', instance.id)
                else:
                    print('Exiting from the given tasks')
        except botocore.exceptions.NoRegionError:
            print(f'You have inputted an invalid region name ')
            sys.exit(2)
        except Exception as exe:
            print(exe)
            sys.exit(3)

    @staticmethod
    def start_instances():
        try:
            ec2_ids = ListEC2Instances().display_ec2()

            if len(ec2_ids['instances_ids']) > 0:
                input_region_name = input(
                    "Please enter the corresponding region name if you want to start all instances for a region")
                input_ec2_id = input(
                    "Please enter the instance id if you want to start a particular instance in the above "
                    "specified region")
                print(input_region_name)
                print(ec2_ids['regions'])
                if input_region_name in ec2_ids['regions']:
                    if input_ec2_id == 'all':
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        # Get only running instances
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-state-name',
                                      'Values': ['stopped']}])
                        # Start the instances
                        for instance in instances:
                            print(f'Starting instance {instance.id}')
                            instance.start()
                            instance.wait_until_running()
                            print('Started instance: ', instance.id)
                    elif len(input_ec2_id.strip('\n').split(',')) > 0:
                        input_ec2_ids = input_ec2_id.strip('\n').split(',')
                        ec2 = management_cons.resource('ec2', region_name=input_region_name)
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-id',
                                      'Values': input_ec2_id.strip('\n').strip(' ').split(',')}])
                        # Start the instances
                        for instance in instances:
                            print(f'Starting instance {instance.id}')
                            instance.start()
                            instance.wait_until_running()
                            print('Started instance: ', instance.id)
                else:
                    print('Exiting from the given tasks')
        except botocore.exceptions.NoRegionError:
            print(f'You have inputted an invalid region name')
            sys.exit(2)
        except Exception as exe:
            print(exe)
            sys.exit(3)

    @classmethod
    def list_instances(cls):
        try:
            # Fetch the EC2 client
            ec2_cli = management_cons.client(service_name='ec2')

            # Fetch all the region names
            regions = ec2_cli.describe_regions()['Regions']
            region_names = [region['RegionName'] for region in regions]

            # account_id = management_cons.client(service_name='sts').get_caller_identity()['Account']
            # print(account_id)
            # pp = pprint.PrettyPrinter(indent=4)

            instance_states = ['pending', 'running', 'shutting-down', 'terminated', 'stopping', 'stopped']

            # Iterate over all regions and pick all the instances grouped by their state
            # Return the instance ids and regions in a dictionary format
            for region_name in region_names:
                ec2 = boto3.resource('ec2', region_name=region_name)

                for each_state in instance_states:
                    # Get only instances for that particular state
                    instances = ec2.instances.filter(
                        Filters=[{'Name': 'instance-state-name',
                                  'Values': [each_state]}])
                    id_count = 0
                    for instance in instances:
                        id_count += 1

                        if id_count == 1:
                            print(
                                f'Printing the instances which are in the state: {each_state}, for the region: {region_name}')
                        print("Instance Id:", instance.id)

        except Exception as exe:
            print(exe)

    @classmethod
    def create_snapshot(cls):
        try:
            EC2lifecycle.list_instances()

            instance_id = input('Please enter the instance id for which you want to create the instance: ')
            region_name = input('Please enter the region name')
            exclude_boot_volume = False

            ec2_res = management_cons.resource('ec2', region_name=region_name)

            # Create the timestamp, this will be included within the boot volume to denote the timestamp
            timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

            instances = ec2_res.instances.filter(InstanceIds=[instance_id])

            for instance in instances.all():
                for vol in instance.volumes.all():
                    desc = "Backup of {0}, created on {1}".format(instance.id, timestamp)
                    print(desc)
                    snapshot = vol.create_snapshot(Description=desc)

                    print("Created snapshot: ", snapshot)

        except Exception as exe:
            print(exe)

    @classmethod
    def prune_snapshots(cls):
        try:

            MENU_PROMPT = '''
- Enter "a" to to delete snapshots based on the snapshot-ids
- Enter "b" to to delete snapshots based on the AWS Account Id
- Enter "c" to delete the snapshots based on the start-time
- Enter "d" to delete the snapshots based on the status (pending | completed | error)
- Enter "e" to delete snapshots based on the tags
 '''
            user_choice = input(MENU_PROMPT)

            if user_choice in 'a':
                snapshot_ids = input("Please enter the snapshot ids, enter multiple snapshots seperated by comma") \
                    .strip(' ').strip('\n').split(',')
                region_name = input("Please enter the region name")

                # Fetch the EC2 client
                ec2_cli = management_cons.client(service_name='ec2', region_name=region_name)
                # ec2_res = management_cons.resource(service_name='ec2')
                delete_snapshots_by_ids(ec2_cli, snapshot_ids)

            elif user_choice in 'b':
                account_id = input("Please enter the account id: ") \
                    .strip(' ').strip('\n')
                region_name = input("Please enter the region name: ")

                # Fetch the EC2 client
                ec2_cli = management_cons.client(service_name='ec2', region_name=region_name)
                # ec2_res = management_cons.resource(service_name='ec2')
                snapshots = ec2_cli.describe_snapshots(
                    Filters=[
                        {
                            'Name': 'owner-id',
                            'Values': [account_id]
                        }
                    ])['Snapshots']

                snapshot_ids = [snapshot['SnapshotId'] for snapshot in snapshots]
                delete_snapshots_by_ids(ec2_cli, snapshot_ids)

            elif user_choice in 'c':
                day_in_num = input('Please enter how many days old snapshots you want to delete?')
                region_name = input("Please enter the region name: ")

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

                    date_range = calculate_date_with_today_date(day_in_num)

                    new_snapshots = snapshots
                    for snapshot in snapshots:
                        # Remove the timezone info
                        if snapshot['StartTime'] > date_range.replace(tzinfo=tzutc()):
                            new_snapshots.remove(snapshot)

                    snapshot_ids = [snapshot['SnapshotId'] for snapshot in new_snapshots]
                    delete_snapshots_by_ids(ec2_cli, snapshot_ids)

                except Exception as exe:
                    print(exe)

            elif user_choice in 'd':
                status = input('Please enter the status for which you want to delete the snapshots?')
                region_name = input("Please enter the region name: ")

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

                    new_snapshots = [snapshot for snapshot in snapshots if snapshot['State'] == status]
                    snapshot_ids = [snapshot['SnapshotId'] for snapshot in new_snapshots]
                    delete_snapshots_by_ids(ec2_cli, snapshot_ids)

                except Exception as exe:
                    print(exe)
            elif user_choice in 'e':
                pass

            else:
                pass

        except Exception as e:
            print(e)

    @classmethod
    def delete_unattached_volumes(cls):
        region_name = input("Please enter the region name: ")

        try:
            ec2_res = management_cons.resource(service_name='ec2', region_name=region_name)
            account_id = management_cons.client(service_name='sts').get_caller_identity()['Account']

            volumes = ec2_res.volumes.filter(
                Filters=[
                    {
                        'Name': 'status', 'Values': ['available']
                    }
                ])

            for volume in volumes:
                v = ec2_res.Volume(volume.id)
                print("Deleting the EBS volume: {0}, Size: {1}".format(volume.id, volume.size))
                v.delete()

        except Exception as exe:
            print(exe)


def calculate_date_with_today_date(day_in_num):
    print(datetime.today().utcnow())  # print today's date time
    new_date = datetime.today().utcnow() - timedelta(days=int(day_in_num))
    print(new_date)  # print new date time after addition of days to the current date
    return new_date
