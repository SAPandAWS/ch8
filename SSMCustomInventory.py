import boto3
import json
import subprocess
import os
import re
import hdbcli

# Retrieve system information using subprocess or other methods
def get_OS_info():
    # Use OS Commands to extract OS level information
    hostname = 'hostname'
    os_vendor = 'os_vendor'
    os_level = 'os_level'
    os_cpu_num = 'cpu_num'
    os_memory_size = 'memory_size'
    
    # Return the derived values
    return hostname, os_vendor, os_level, os_cpu_num, os_memory_size
   
# Retrieve EC2 instance details from IMDS Service
def get_EC2_info():
    # Use IMDS to retrieve EC2 metadata information
    ec2_type = 'instance_type'
    instance_id = 'instance_id'
    
    # Return the derived values
    return ec2_type, instance_id

# Retrieve SAP Application details
def get_SAP_info():
    # Execute sapcontrol OS command to get instance type and number
    sid = 'sid'
    sap_instance_details = 'sap_instance_details'
    sap_kernel = 'sap_kernel'
    sap_component_details = 'sap_component_details'
    
    # Return the derived values
    return sid, sap_instance_details, sap_kernel, sap_component_details

# Retrieve DB Application details
def get_DB_info():
    # Connect database using respective DB library (ex. hdbcli for SAP HANA)
    # Run database queries to extract DB information
    db_type = 'db_type'
    db_level = 'db_level'
    db_size = 'db_size'  
    
    # Return the derived values
    return db_type, db_level, db_size

# Collate all the information into a single object
def get_system_info():
    # Retrieve OS info
    hostname, os_vendor, os_level, os_cpu_num, os_memory_size = get_OS_info()
    # Retrieve EC2 info
    ec2_type, instance_id = get_EC2_info()
    # Retrieve SAP info
    sid, sap_instance_details, sap_kernel, sap_component_details = get_SAP_info()
    # Retrieve DB info
    db_type, db_level, db_size = get_DB_info()

    return {
        'hostname': hostname,
        'os_vendor': os_vendor,
        'os_level': os_level,
        'os_cpu_num': os_cpu_num,
        'os_memory_size': os_memory_size,
        'ec2_type': ec2_type,
        'instance_id': instance_id,
        'sid': sid,
        'sap_instance_details': sap_instance_details,
        'sap_kernel': sap_kernel,
        'sap_component_details': sap_component_details,
        'db_type': db_type,
        'db_level': db_level,
        'db_size': db_size
    }

# Update the JSON document with gathered system information
def update_json_document(system_info):
    json_document = {
        "SchemaVersion": "1.0",
        "TypeName": "Custom:SAP",
        "Content": system_info
    }
    return json_document

# Main function
def main():
    system_info = get_system_info()
    updated_json_document = update_json_document(system_info)
	#Store the JSON document at the SSM Custom Inventory location
	
if __name__ == "__main__":
    main()
