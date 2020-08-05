import boto3

aws_mgmt_con = boto3.session.Session(profile_name='administrator')

ec2_resources = aws_mgmt_con.resource(service_name='ec2')

dir(ec2_resources)

for ec2_instance in ec2_resources.instances.all():
    print(ec2_instance)