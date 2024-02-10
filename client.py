"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/10/2024
    File Name: client.py
    Project Name: PyFileTransfer
"""

# Python Standard Library Imports.
import socket

# Project Imports.
from packets import ClientFilePacket
from utils import gui_get_file

def await_message(current_socket, text): # Wait until the desired message is recieved. 
    while True:
        server_data = current_socket.recv(1024)
        if server_data.decode('utf-8') == text:
            print(text)
            return True

my_socket = socket.socket()

try:
    my_socket.connect(("127.0.0.1", 1234))  
    print("Waiting for connection to be accepted... ") # Wait for the server to accept the connection.
    await_message(my_socket, "Connection accepted")
    while True: # Continue until no file is selected.
        file_path, file_name = gui_get_file() # Request a file for transfer.
        if file_path != "":
            with open(file_path, 'rb') as file_obj: # Get the binary of the file.
                file_data = file_obj.read()
            my_packet = ClientFilePacket(my_socket.getsockname(), file_name, file_data) # Create and send a packet containing the file and data.
            my_socket.sendall(repr(my_packet).encode())
            await_message(my_socket, f"Server Recieved {file_name}.") # Wait for server to confirm successful file transfer.
        else: # No file was selected for transfer. End the connection.
            my_socket.close()
            break
except ConnectionRefusedError:
    print("Server disconnected or does not exist.")        
