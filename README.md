## Steps to Create an AWS EC2 instance:

As for new AWS accounts, we can't create a classic EC2, but it should be created inside a VPC.

So we need to do the following:

1- Create a VPC with the desired IP range.
2- Create subnet/s with IP ranges 
3- Create an internet gateway 
4- Create route table for public subnet, also another for private subnet if needed. 
5- Create security group that will be assigned to the instance 
6- create the instance and update it's DNS record.

** The above is automated in an Ansible playbook in role named "provision_aws_infra" and every task has a name field to describe what it's doing.

#### Steps for running the playbook ####

## Requirements: 
	Ansible 2.5.0
	python boto3 library

## Set credentials, change xxxxxxxxxx with your aws keys
 
>>> export AWS_ACCESS_KEY_ID='xxxxxxxxxx'
>>> export AWS_SECRET_ACCESS_KEY='xxxxxxxxxx'

## Clone the repo, then run the playbook

>>> cd in_to_the_repo 
>>> ansible-playbook -i local, provision_ec2.yml

## Run the monitoring Script:
#you need to have requests module installed.

>>> python check_website.py

Script output: is a message in case of success or faliure of the check, plus an exit status code for each case.
0 > for OK / passed check,
1 > if server responds with 200, but with invalid content and, 
2 > for faliures, either server is unreachable or web server is down.

===========================
===========================
===========================
Careship - DevOps Challenge
===========================

# Objectives

- Automate the creation of a web server
- Automate the server health check

# Prerequisites

- You will need an AWS account.
  - Create one if you don't own one already, you can use free-tier resources for this challenge.

# The Challenge

Set up a new EC2 instance in AWS.

It must:

* Be publicly accessible.
* Run Nginx.
* Serve a `/version.txt` file, containing only static text representing a version number, ```1.7.0``` for example.

# Mandatory Work

Fork this repository.

* Provide instructions on how to create the server.
* Provide a script that can be run periodically (and externally) to check if the server is up and serving the expected version number. Use your scripting language of choice.
* Alter the README to contain the steps required to:
  * Create the server.
  * Run the health check script.
* Provide us IAM credentials to login to the AWS account. If you have other resources in it make sure we can only access what is related to this test.

Send us an email when you’re done. Feel free to ask questions if anything is unclear, confusing, or just plain missing.

# Extra Credit

We know time is precious, we won't mark you down for not doing the extra credits, but if you want to give them a go...

* Use a CloudFormation template to set up the server.
* Use a configuration management tool (such as Puppet, Chef or Ansible) to bootstrap the server.
* Put the server behind a load balancer (it can be a reverse proxy with Nginx, if you will).
* Run Nginx inside a Docker container.
* Make the checker script SSH into the instance, check if Nginx is running and start it if it isn't.

# Questions

#### What scripting languages can I use?

Anyone you like. You’ll have to justify your decision. Please pick something you're familiar with.

#### Will I have to pay for the AWS charges?

No. You are expected to use free-tier resources only and not generate any charges. Please remember to delete your resources once the review process is over so you are not charged by AWS.

#### What will you be grading me on?

Scripting skills, elegance, understanding of the technologies you use, security, documentation.

#### Will I have a chance to explain my choices?

Feel free to comment your code, or put explanations in a pull request within the repo.
If we proceed to a phone interview, we’ll be asking questions about why you made the choices you made.

#### Why doesn't the test include X?

Good question. Feel free to tell us how to make the test better. Or, you know, fork it and improve it!
