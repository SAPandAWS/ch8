import boto3
import json
def lambda_handler(event, context):
    # Initialize AWS Config client
    config_client = boto3.client('config')

    # Define the desired instance type for SAP workloads
    desired_instance_type = 'm6i.xlarge'
    
    # Parse the invoking event to get the EC2 instance ID
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']
    instance_id = configuration_item['resourceId']
    
    # Check if the instance type matches the desired type
    compliance = 'COMPLIANT' if configuration_item['configuration']['instanceType'] == desired_instance_type else 'NON_COMPLIANT'
    
    # Prepare the evaluation for AWS Config
    evaluation = {
        'ComplianceResourceType': invoking_event['configurationItem']['resourceType'],
        'ComplianceResourceId': instance_id,
        'ComplianceType': compliance,
        'OrderingTimestamp': configuration_item['configurationItemCaptureTime']
    }

    # Put the evaluation results
    response = config_client.put_evaluations(
        Evaluations=[evaluation],
        ResultToken=event['resultToken']  # Token provided by the event
    )
    return response
