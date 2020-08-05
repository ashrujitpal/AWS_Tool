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
                input_ec2_id = input("Please enter the instance id if you want to stop a particular instance in the above "
                                     "specified region, to enter multiple instances, seperate them with comma")

                if input_region_name in ec2_ids['regions']:
                    if input_ec2_id == 'all':
                        ec2 = boto3.resource('ec2', region_name=input_region_name)
                        # Get only running instances
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-state-name',
                                      'Values': ['started']}])
                        # Start the instances
                        for instance in instances:
                            instance.stop()
                            print('Stopped instance: ', instance.id)
                    elif len(input_ec2_id.strip('\n').split(',')) > 0:
                        input_ec2_ids = input_ec2_id.strip('\n').split(',')
                        ec2 = boto3.resource('ec2', region_name=input_region_name)
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-id',
                                      'Values': input_ec2_id.strip('\n').strip(' ').split(',')}])
                        # Start the instances
                        for instance in instances:
                            instance.stop()
                            print('Stopped instance: ', instance.id)
                else:
                    print('Exiting from the given tasks')
        except botocore.exceptions.NoRegionError:
            print(f'You have inputted an invalid region name')
            sys.exit(2)
        except Exception as exe:
            print(exe)
            sys.exit(3)

    @staticmethod
    def terminate_instances():
        ListEC2Instances().display_ec2()

    @staticmethod
    def reboot_instances():
        ListEC2Instances().display_ec2()

    @staticmethod
    def start_instances():
        try:
            ec2_ids = ListEC2Instances().display_ec2()
            if len(ec2_ids['instances_ids']) > 0:
                input_region_name = input(
                    "Please enter the corresponding region name if you want to start all instances for a region")
                input_ec2_id = input("Please enter the instance id if you want to start a particular instance in the above "
                                     "specified region")

                if input_region_name in ec2_ids['regions']:
                    if input_ec2_id == 'all':
                        ec2 = boto3.resource('ec2', region_name=input_region_name)
                        # Get only running instances
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-state-name',
                                      'Values': ['stopped']}])
                        # Start the instances
                        for instance in instances:
                            instance.start()
                            print('Started instance: ', instance.id)
                    elif len(input_ec2_id.strip('\n').split(',')) > 0:
                        input_ec2_ids = input_ec2_id.strip('\n').split(',')
                        ec2 = boto3.resource('ec2', region_name=input_region_name)
                        instances = ec2.instances.filter(
                            Filters=[{'Name': 'instance-id',
                                      'Values': input_ec2_id.strip('\n').strip(' ').split(',')}])
                        # Start the instances
                        for instance in instances:
                            instance.start()
                            print('Started instance: ', instance.id)
                else:
                    print('Exiting from the given tasks')
        except botocore.exceptions.NoRegionError:
            print(f'You have inputted an invalid region name')
            sys.exit(2)
        except Exception as exe:
            print(exe)
            sys.exit(3)