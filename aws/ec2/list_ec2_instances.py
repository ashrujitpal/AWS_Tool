import sys
import boto3
import botocore
import pprint

profile = 'administrator'

try:
    management_cons = boto3.session.Session(profile_name=profile)
except botocore.exceptions.ProfileNotFound:
    print(f'The config profile ({profile}) could not be found')
except Exception as e:
    print(e)
    sys.exit()


class ListEC2Instances:

    @staticmethod
    def display_ec2():

        MENU_PROMPT = '''
- Enter "a.a" to to list stopped instances region wise
- Enter "a.b" to to list started instances region wise
- Enter "b.a" to list the stopped instances with tags
- Enter "b.b" to list the started instances with tags
- Enter "c" to list the instances with instance-lifecycle
- Enter "d" to list the instances with instance-state-name
- Enter "e" to list the instances with instance-type
- Enter "f" to list the instances with the vpc-id
'''

        selection = input(MENU_PROMPT)

        while selection != 'q':
            if selection in 'a.a':
                # List all the instances region wise
                return ListEC2Instances.list_stopped_instance_region_wise()

            if selection in 'a.b':
                # List all the instances region wise
                return ListEC2Instances.list_running_instance_region_wise()

            elif selection in 'b.a':
                # List all the stopped instances with a tag name
                return ListEC2Instances.list_stopped_instance_tag_wise()

            elif selection in 'b.b':
                # List all the started instances with a tag name
                return ListEC2Instances.list_running_instance_tag_wise()

            elif selection in 'c':
                # List all the instances with life cycles
                return ListEC2Instances.list_instance_lifecycle_wise()

            elif selection in 'd':
                # List all the instances with states
                return ListEC2Instances.list_instance_state_wise()

            elif selection in 'e':
                # List all the instances with instance types
                return ListEC2Instances.list_instance_type_wise()

            elif selection in 'd':
                # List all the instances with based on the vpc-id
                return ListEC2Instances.list_instance_vpc_wise()
            else:
                print('Unknown command. Please try again.')

            selection = input(MENU_PROMPT)

    '''
    This method will list all the instances based on the regions
    It will print the instance ids against each regions    
    '''

    @staticmethod
    def list_stopped_instance_region_wise():

        try:
            # Fetch the EC2 client
            ec2_cli = management_cons.client(service_name='ec2')

            # Fetch all the region names
            regions = ec2_cli.describe_regions()['Regions']
            region_names = [region['RegionName'] for region in regions]

            # account_id = management_cons.client(service_name='sts').get_caller_identity()['Account']
            # print(account_id)
            # pp = pprint.PrettyPrinter(indent=4)

            print("Below instances are currently in the stopped state:")

            # Create a list to store the instance ids region wise
            instance_ids = []

            # Iterate over all regions and pick only those instance ids which are in stopped state
            # Return the instance ids and regions in a dictionary format
            for region_name in region_names:
                ec2 = boto3.resource('ec2', region_name=region_name)
                # Get only stopped instances
                instances = ec2.instances.filter(
                    Filters=[{'Name': 'instance-state-name',
                              'Values': ['stopped']}])
                count = 0
                for instance in instances:
                    print("Instance Id:", instance.id)
                    instance_ids.append(instance.id)
                    count += 1
                if count > 0:
                    print("Region Name:", region_name)
                    print("=======================================================")
            return {'instances_ids': instance_ids, 'regions': region_names}

        except Exception as exe:
            print(exe)
            sys.exit()

    '''
        This method will list all the instances based on the regions
        It will print the instance ids against each regions    
    '''

    @staticmethod
    def list_running_instance_region_wise():

        try:
            # Fetch the EC2 client
            ec2_cli = management_cons.client(service_name='ec2')

            # Fetch all the region names
            regions = ec2_cli.describe_regions()['Regions']
            region_names = [region['RegionName'] for region in regions]

            print("Below instances are currently in the started state:")

            # Create a list to store the instance ids region wise
            instance_ids = []

            # Iterate over all regions and pick only those instance ids which are in started state
            # Return the instance ids and regions in a dictionary format
            for region_name in region_names:
                ec2 = boto3.resource('ec2', region_name=region_name)
                # Get only stopped instances
                instances = ec2.instances.filter(
                    Filters=[{'Name': 'instance-state-name',
                              'Values': ['running']}])
                count = 0
                for instance in instances:
                    print("Instance Id:", instance.id)
                    instance_ids.append(instance.id)
                    count += 1
                if count > 0:
                    print("Region Name:", region_name)
                    print("=======================================================")

            return {'instances_ids': instance_ids, 'regions': region_names}
        except Exception as exe:
            print(exe)
            sys.exit()

    @staticmethod
    def list_stopped_instance_tag_wise():

        try:
            # Fetch the EC2 client
            ec2_cli = management_cons.client(service_name='ec2')

            # Fetch all the region names
            regions = ec2_cli.describe_regions()['Regions']
            region_names = [region['RegionName'] for region in regions]

            tag_name = input('Please enter the tag name')
            tag_value = input('Please enter the tag value')
            tag_name = f'tag:{tag_name}'
            print(tag_name)
            print("Below instances are currently in the stopped state:")

            # Create a list to store the instance ids region wise
            instance_ids = []

            # Iterate over all regions and pick only those instance ids which are in stopped state
            # Return the instance ids and regions in a dictionary format
            for region_name in region_names:
                ec2 = boto3.resource('ec2', region_name=region_name)
                # Get only stopped instances
                instances = ec2.instances.filter(
                    Filters=[{'Name': tag_name,
                              'Values': [tag_value]}])
                count = 0
                for instance in instances:
                    print("Instance Id:", instance.id)
                    instance_ids.append(instance.id)
                    count += 1
                if count > 0:
                    print("Region Name:", region_name)
                    print("=======================================================")

            return {'instances_ids': instance_ids, 'regions': region_names}
        except Exception as exe:
            print(exe)
            sys.exit()

    '''
        This method will list all the instances based on the regions
        It will print the instance ids against each regions    
    '''

    @staticmethod
    def list_running_instance_tag_wise():

        try:
            # Fetch the EC2 client
            ec2_cli = management_cons.client(service_name='ec2')

            # Fetch all the region names
            regions = ec2_cli.describe_regions()['Regions']
            region_names = [region['RegionName'] for region in regions]

            print("Below instances are currently in the started state:")

            # Create a list to store the instance ids region wise
            instance_ids = []

            # Iterate over all regions and pick only those instance ids which are in started state
            # Return the instance ids and regions in a dictionary format
            for region_name in region_names:
                ec2 = boto3.resource('ec2', region_name=region_name)
                # Get only stopped instances
                instances = ec2.instances.filter(
                    Filters=[{'Name': 'instance-state-name',
                              'Values': ['running']}])
                count = 0
                for instance in instances:
                    print("Instance Id:", instance.id)
                    instance_ids.append(instance.id)
                    count += 1
                if count > 0:
                    print("Region Name:", region_name)
                    print("=======================================================")

            return {'instances_ids': instance_ids, 'regions': region_names}
        except Exception as exe:
            print(exe)
            sys.exit()


    def list_instance_lifecycle_wise(self):
        pass

    def list_instance_state_wise(self):
        pass

    def list_instance_type_wise(self):
        pass

    def list_instance_vpc_wise(self):
        pass
