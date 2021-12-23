import socket
#importing the socket library

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    #making a simple socket AF_INET refers to the ipv4 address family and SOCK_stream means connection oriented TCP protocol
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'end':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()