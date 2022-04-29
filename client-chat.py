from http import client
from threading import *
import socket,time,pickle,json


class Client_chat_Application:
    socket_address = 0
    port_number=0
    def __init__(self):
        super().__init__()
        self.ClientSocket = socket.socket()
    
    def Build_connection(self):
        client_name = "Its chandu !"
        try:
            self.ClientSocket.connect((Client_chat_Application.socket_address,Client_chat_Application.port_number))
            self.ClientSocket.send(bytes(client_name,'utf-8'))
          
            self.Response_receiver()
        except Exception as SocketErr01:
            print(f"Error in Biulding connection : {SocketErr01}")
    
    def Response_receiver(self):
        '''Listing Server response'''
        try:
            while True:
                print("[02]:: Waiting For Response...\n") # -------To be deleted In production
                self.Response = self.ClientSocket.recv(1024*6)
                self.Response = pickle.loads(self.Response[10:])
                print(self.Response["Notifier"])
                
                # Response = self.Response
        except Exception as e:
            print(f"Error in Response receiver : {e}")

if __name__ == "__main__":
    ClientChatApp = Client_chat_Application()
    Client_chat_Application.socket_address = "192.168.50.9"
    Client_chat_Application.port_number = 9999

    ClientChatApp.Build_connection()