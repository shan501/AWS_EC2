# AWS_EC2


## This is a python script used to automate configutation and processes of AWS ec2 using Boto3 
This python script includes creating a key to ssh into instance , creating a security group with inbound rules , and a ec2 with these two attached 


## To start
To start you would need to create a user in AWS. Allow for programmatic access.Then set the access you want for that user 
Aws will then provide you with a access and private key.Save both for use later. 

run this command and put in the access and private key 

```
aws configure 

```
now you would just need to install boto3 and aws cli

```
pip3 install boto3 
pip3 install awscli

``` 

Now you can start coding 
