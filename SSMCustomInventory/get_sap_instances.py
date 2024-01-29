import subprocess
import re

def find_sap_instances():
    #Function to find all SAP instances running on the host.

    sap_instances = []
    try:
        # Execute the command to get processes related to SAP
        command = "ps -eaf | grep sap"
        process_list = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

        # Regular expression to match typical SAP instance process names
        # This pattern might need to be adjusted based on your specific SAP environment
        sap_instance_pattern = re.compile(r'sap\S+')

        # Search for SAP instance names in the process list
        for line in process_list.stdout.split('\n'):
            match = sap_instance_pattern.findall(line)
            if match:
                sap_instances.extend(match)

        # Remove duplicates and return the list of SAP instances
        return list(set(sap_instances))

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching SAP process list: {e}")
        return []

if __name__ == "__main__":
    # Find and print all SAP instances
    instances = find_sap_instances()
    if instances:
        print("SAP Instances running on the host:")
        for instance in instances:
            print(instance)
    else:
        print("No SAP instances found or unable to retrieve process list.")
