# import socket programming library
import socket
# import thread module
from _thread import *
import threading
#mac address 
import re,uuid
  
print_lock = threading.Lock()
  
# thread function
def threaded(c):
    while True:
  
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
              
            # lock released on exit
            print_lock.release()
            break
  
        # reverse the given string from client
        data = data[::-1]
  
        # send back reversed string to client
        c.send(data)
  
    # connection closed
    c.close()
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    print("socket binded to port", port)

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)

    while True:
        conn, address = server_socket.accept()  # accept new connection
    
        # lock acquired by client
        print_lock.acquire()

        print("----------------------------")
        print('Connected to :', address[0], ':', address[1])
        print("Protocol: TCP \nApplication: HTTP")
        print ("The MAC address in formatted is : ", end="") 
        print (':'.join(re.findall('..', '%012x' % uuid.getnode()))) 
        print("----------------------------")

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

        # Start a new thread and return its identifier
        start_new_thread(threaded, (conn,))
        
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
