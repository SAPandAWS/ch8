import subprocess

def get_hostname():
    # Function to retrieve the hostname of the system using subprocess.
    
    try:
        # Using subprocess to execute the 'hostname' command
        result = subprocess.run(['hostname'], check=True, stdout=subprocess.PIPE, universal_newlines=True)

        # Extracting the hostname from the command output
        hostname = result.stdout.strip()

        return hostname
    except subprocess.CalledProcessError as e:
        # Handle exceptions if the subprocess call fails
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Retrieve and print the hostname
    hostname = get_hostname()
    if hostname:
        print(f"The hostname of the system is: {hostname}")
    else:
        print("Failed to retrieve the hostname.")
