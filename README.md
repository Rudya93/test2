# test2

Prerequisites:


Create three A or CNAME records for the custom domain (like a.domain.com, b.domain.com, c.domain.com). If you don’t have one, please register free in pp.ua zone.

Point them to three EC2 instances: 2xEC2 should be running, 1xEC2 should be in stopped state.


Task definition:


Write a Shell/Python script using AWS SDK that will do the following:


1. Determine the instance state using its DNS name (need at least 2 verifications: TCP and HTTP).

2. Create an AMI of the stopped EC2 instance and add a descriptive tag based on the EC2 name along with the current date.

3. Terminate stopped EC2 after AMI creation.

4. Clean up AMIs older than 7 days.

5. Print all instances in fine-grained output, INCLUDING terminated one, with highlighting their current state.
