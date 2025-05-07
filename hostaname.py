import socket

def get_hostname():
    return socket.gethostname()

def main():
    current_hostname = get_hostname()
    print(f"Current hostname: {current_hostname}")

if __name__ == "__main__":
    main()
