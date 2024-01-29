import subprocess
import re

def get_sap_kernel_version(instance_number):
    #Get the SAP kernel version using the sapcontrol's GetVersionInfo web method.
    # sapcontrol -nr <InstanceNumber> -function GetVersionInfo
    try:
        # Construct the sapcontrol command
        command = ["sapcontrol", "-nr", str(instance_number), "-function", "GetVersionInfo"]

        # Execute the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

        # Regular expression to match the kernel version
        kernel_version_pattern = re.compile(r'kernel release\s+(\d+\.\d+\.\d+)', re.IGNORECASE)

        # Search for the kernel version in the command output
        match = kernel_version_pattern.search(result.stdout)
        if match:
            return match.group(1)
        else:
            print("SAP kernel version not found in the output.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing sapcontrol: {e}")
        return None

if __name__ == "__main__":
    instance_number = 0  # Replace with your SAP instance number
    kernel_version = get_sap_kernel_version(instance_number)
    if kernel_version:
        print(f"The SAP kernel version is: {kernel_version}")
    else:
        print("Failed to retrieve the SAP kernel version.")
