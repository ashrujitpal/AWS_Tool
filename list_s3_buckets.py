import boto3
import botocore
import pprint

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(dir(boto3.exceptions))
print("=======================================\n")
pp.pprint(dir(botocore.exceptions))

aws_mgmt_con = boto3.session.Session(profile_name='administrator')
aws_s3_res = aws_mgmt_con.resource('s3')

for bucket in aws_s3_res.buckets.all():
    print(bucket)
    