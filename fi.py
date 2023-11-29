import paramiko
import sys

def connect_ssh(host, port, username, password):
    try:
        # Register SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect
        client.connect(host, port=port, username=username, password=password, timeout=1)
        print("Authentication success")

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        # Close the client in all cases
        client.close()

# Set args
host = sys.argv[1]
port = int(sys.argv[2])
username = sys.argv[3]
password = sys.argv[4]

# Call the function
connect_ssh(host, port, username, password)
