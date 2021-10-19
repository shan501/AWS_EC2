#! /usr/bin/env python3 
import boto3, 

#Create a ec2 resource 
ec2=boto3.resource('ec2')

#Create key pair to ssh into instance
key=ec2.create_key_pair(KeyName='SSHKey')



#Store the key in a file called key.pem
with open ("key.pem","w+",encoding='utf-8') as f :
    f.write(key)



#create a security group and attach it to the instance
ec2_client=boto3.client('ec2')
ec2_client.create_security_group(Description="Security Group",
                                GroupName="Testing")


#the security group will allow all inbound traffic
ec2_client.authorize_security_group_ingress(
        GroupId="sg-0f1132523dada655a",
        IpPermissions=[
            {
                'From Port':0,
                'IpProtocol':'-1',
                'IpRanges':[
                    {
                        'CidrIp':'0.0.0.0/0',
                        },
                    ],
                'ToPort':60000,
                }
            ]
        )


#create ec2 instance and attach everything to it
ec2.create_instances(ImageId='ami-013a129d325529d4d',
        InstanceType='t2.micro',
        KeyName='SSHKey',
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            'sg-0f1132523dada655a'
            ],
        )



