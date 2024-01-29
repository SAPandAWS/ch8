


import boto3
def lambda_handler(event, context):
    # Initialize EC2 client
    ec2_client = boto3.client('ec2')

    # Define the desired instance type for SAP workloads
    # Or assign the desired instance based on custom logic
    desired_instance_type = 'm6i.xlarge'

    # Get the instance ID from the AWS Config event
    # This is a simplified extraction, you may need to parse a real event differently
    instance_id = event['detail']['resourceId']

    # Stop the instance before changing the instance type
    ec2_client.stop_instances(InstanceIds=[instance_id])
    
    # Wait for the instance to stop
    waiter = ec2_client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[instance_id])

    # Modify the instance type of the non-compliant EC2 instance
    modify_response = ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        InstanceType={
            'Value': desired_instance_type
        }
    )

    # Start the instance after modifying the instance type
    start_response = ec2_client.start_instances(InstanceIds=[instance_id])
    
    return {
        'modify_response': modify_response,
        'start_response': start_response
    }
