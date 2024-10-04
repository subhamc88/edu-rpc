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


# Taking your request
    method = "add"
    number_1 = 1
    number_2 = 1

    # Only accepts string as input.
    while True:
        user_input_method = input("Enter your method/operation (Only String Allowed): \nadd\nsub\nmultiply\nquotient\nremainder\n")
        if user_input_method in ["add", "sub", "multiply", "quotient", "remainder"]:
            method = user_input_method
            break

    # Only accepts number as input.
    while True:
        user_number_1 = input("Enter your first number (Only Number Allowed): ")
        try:
            number_1 = float(user_number_1)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Only accepts number as input.
    while True:
        user_number_2 = input("Enter your second number (Only Number Allowed): ")
        try:
            number_2 = float(user_number_2)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Response from server: {send_request(method, number_1, number_2)}")
