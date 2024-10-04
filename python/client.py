import json
import socket


def send_request(method, *args):
    '''Function to send a request to the RPC server.'''

    # Create a socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 1331))

    # Prepare the request
    request = json.dumps([method] + list(args))
    client.send(request.encode())

    # Get the response
    response = client.recv(1024).decode()

    client.close()

    return json.loads(response)


if __name__ == "__main__":
    print("Connection to Server")
    print("Adding 10 and 10:", send_request("add", 10, 10))
    print("Subtracting 10 and 10:", send_request("sub", 10, 10))
    print("Multiplying 10 and 10:", send_request("multiply", 10, 10))
    print("Dividing 10 and 10:", send_request("quotient", 10, 10))
    print("Finding Remainder between 10 and 10:", send_request("remainder", 10, 10))
