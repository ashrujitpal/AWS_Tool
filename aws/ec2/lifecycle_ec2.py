from datetime import datetime
import sys
import boto3
import botocore
from aws.ec2.list_ec2_instances import ListEC2Instances

profile = 'administrator'

try:
    management_cons = boto3.session.Session(profile_name=profile)
except botocore.exceptions.ProfileNotFound:
    print(f'The config profile ({profile}) could not be found')
except Exception as e:
    print(e)
    sys.exit(1)


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
