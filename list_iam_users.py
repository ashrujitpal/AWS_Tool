import boto3

aws_mgmt_con = boto3.session.Session(profile_name='administrator')
iam_con = aws_mgmt_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)
