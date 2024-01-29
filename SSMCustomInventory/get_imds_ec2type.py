import requests

def get_instance_type():
    #Function to get the EC2 instance type using the EC2 Instance Metadata Service (IMDS).

    try:
        # Define the URL for the IMDSv2 token
        token_url = "http://169.254.169.254/latest/api/token"

        # Define the headers for the token request
        token_headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}

        # Request a token for IMDSv2
        token_response = requests.put(token_url, headers=token_headers)
        if token_response.status_code != 200:
            raise Exception("Failed to get IMDSv2 token")

        # Define the URL for the instance type metadata
        instance_type_url = "http://169.254.169.254/latest/meta-data/instance-type"

        # Define the headers including the token for the instance type request
        instance_type_headers = {"X-aws-ec2-metadata-token": token_response.text}

        # Request the instance type metadata
        instance_type_response = requests.get(instance_type_url, headers=instance_type_headers)
        if instance_type_response.status_code != 200:
            raise Exception("Failed to get instance type from IMDS")

        # Return the instance type
        return instance_type_response.text

    except requests.RequestException as e:
        # Handle any exceptions that occur during the requests
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Retrieve and print the EC2 instance type
    instance_type = get_instance_type()
    if instance_type:
        print(f"The EC2 instance type is: {instance_type}")
    else:
        print("Failed to retrieve the EC2 instance type.")

