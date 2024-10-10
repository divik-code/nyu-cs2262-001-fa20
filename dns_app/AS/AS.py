import socket

# Dictionary to store hostname with ip address records
host_records = {}

# Method to start the UDP server
def server_startup():
    # Create UDP socket
    as_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_port = 53533
    # Bind the socket to all available interfaces on port 53533
    as_socket.bind(('0.0.0.0', server_port))

    # Continuously listen for incoming UDP requests
    while True:
        # Receive and decode data from client
        data, address = as_socket.recvfrom(2048)
        decoded_lines = data.decode().split('\n')

        # Handle registration request
        if "VALUE" in decoded_lines[2]:
            name = decoded_lines[1].split('=')[1].strip()
            val = decoded_lines[2].split('=')[1].strip()
            host_records[name] = val
            response = f"TYPE=A\nNAME={name}\nVALUE={val}\nTTL=10\n"
            as_socket.sendto(response.encode(), address)
        else:
            # Handle a query request
            name_query = decoded_lines[1].split('=')[1].strip()
            response_value = host_records.get(name_query, 'Not Found')
            response = f"TYPE=A\nNAME={name_query}\nVALUE={response_value}\nTTL=10\n"
            as_socket.sendto(response.encode(), address)

if __name__ == '__main__':
    server_startup()