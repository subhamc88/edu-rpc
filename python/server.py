'''
This is a beginner friendly RPC implementation project.
'''
import json
import socket

# Functions for remote call #


def add(x, y):
    '''
    Basic Addition Function
    '''
    return x+y


def sub(x, y):
    '''
    Function for subtraction.
    '''
    return x - y


def multiply(x, y):
    '''
    Function for subtraction.
    '''
    return x * y


def quotient(x, y):
    '''
    Function for subtraction.
    '''
    return x / y


def remainder(x, y):
    '''
    Function for subtraction.
    '''
    return x % y


# Handlers #


def client_connection_handler(client_socket):
    '''
    Function to handle client connections and execute requested methods.
    '''
    try:
        # Decoding client json request.
        request = client_socket.recv(1024).decode()

        # Method and argument separation from the request.
        method, *args = json.loads(request)

        # Convert arguments to float for arithmetic operations
        args = list(map(float, args))

        # Defining server response based on the client request method.
        if method == "add":
            response = add(*args)
        elif method == "sub":
            response = sub(*args)
        elif method == "multiply":
            response = multiply(*args)
        elif method == "quotient":
            response = quotient(*args)
        elif method == "remainder":
            response = remainder(*args)
        else:
            response = "Method invalid."

        # Send response back to client
        client_socket.send(json.dumps(response).encode())

    except Exception as err:
        client_socket.send(json.dumps(f"Error: {str(err)}").encode())
    finally:
        client_socket.close()


# Server Setup #


def run_server(host='localhost', port=1331):
    '''
    Function to run the server.
    '''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Listening on {host}:{port}...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        client_connection_handler(client_socket)


if __name__ == "__main__":
    print("Starting server...")

    # Add parameters to change the 'host name' and the 'port number'.
    run_server()
