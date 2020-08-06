import boto3
from datetime import datetime

management_cons = boto3.session.Session(profile_name='administrator')

try:

    instance_id = 'i-029b84427a16e0630' #input('Please enter the instance id for which you want to create the instance: ')

    region_name = 'us-east-1' #input('Please enter the region name')
    exclude_boot_volume = False

    ec2_res = management_cons.resource('ec2', region_name=region_name)

    # Create the timestamp, this will be included within the boot volume to denote the timestamp
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    instances = ec2_res.instances.filter(InstanceIds=[instance_id])

    for i in instances.all():
        v = i.volumes.all()
        print(v.id)

    '''
    for vol in instance.volumes().all():
        desc = "Backup of {0}, volume {1}, created on {2}".format(instance.id, vol.id, timestamp)
        print(desc)
        snapshot = vol.create_snapshot(Desccription=desc)

        print("Created snapshot: ", snapshot)'''

except Exception as exe:
    print(exe)
