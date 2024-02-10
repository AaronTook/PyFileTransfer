"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/10/2024
    File Name: packets.py
    Project Name: PyFileTransfer
"""

class ClientFilePacket():
    """ Represent a packet to be sent from the Client to Server transferring a file. """
    def __init__(self, sender, file_name, data): # Object constructor.
        self.sender = sender
        self.file_name = file_name
        self.data = data
    def get_data(self):# Getter for the .data field.
        return self.data
    def get_file_name(self): # Getter for the .file_name field.
        return self.file_name
    def get_sender(self): # Getter for the .sender field.
        return self.sender
    def __str__(self, show_data = True): # Display a string representation of the object with or without the binary file data.
        if show_data:
            return (f"{self.sender} sent {self.file_name}:\n {self.data}")
        else:
            return (f"{self.sender} sent {self.file_name}.")
    def __repr__(self): # Represent the object as a string that can generate the object using eval().
        return f"ClientFilePacket({self.sender}, \"{self.file_name}\", %r)" % self.data