"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/10/2024
    File Name: server.py
    Project Name: PyFileTransfer
"""

# Python Standard Library Imports.
import socket
import os

# Project Imports.
from packets import ClientFilePacket

my_socket = socket.socket()
my_socket.bind(("127.0.0.1",1234))
my_socket.listen()
print("Server started. Now listening for connections...")
while True: # Get one client connection at a time.
    connection, address = my_socket.accept() # Accept the connection.
    connection.sendall("Connection accepted".encode('utf-8')) # Inform the client of the connection in case they tried to connect during the inner while loop.
    print(f"Client connected: {address}")
    message = ""
    while True: # Process the current client connection.
        client_data = connection.recv(1024) # Get up to 1024 bytes of data from the client at a time.
        message += client_data.decode() # Add the data to the current set of data (used when more than 1024 bytes of total data is necessary for one action).
        if len(client_data) < 1024: # The entire action is less than 1024 bytes.
            if not client_data and message == "": # There is not additional data from previous data sets in the action and the user wants to disconnect.
                print("Client disconnected.")
                break # Return to awaiting a client connection.
            else: # The data for this action is complete.
                client_packet = eval(message)
                output_dir = os.path.join(os.getcwd(), "Recieved")
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                print(client_packet.__str__(show_data=False)) # Display the action summary.
                with open(os.path.join(output_dir, client_packet.get_file_name()), 'wb') as file_obj: # Create the transferred file.
                    file_obj.write(client_packet.get_data())
                connection.sendall(f"Server Recieved {client_packet.get_file_name()}.".encode('utf-8'))
                message = "" # Start a new action.
