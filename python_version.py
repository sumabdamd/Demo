import socket
import sys

def get_hostname():
    return socket.gethostname()

def get_python_version():
    version = sys.version_info
    return f"{version.major}.{version.minor}.{version.micro}"

def main():
    current_hostname = get_hostname()
    python_version = get_python_version()
    
    print(f"Current hostname: {current_hostname}")
    print(f"Running Python version: {python_version}")

if __name__ == "__main__":
    main()
