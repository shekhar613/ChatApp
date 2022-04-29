from threading import *
import socket,time,pickle,json

class Chat_Application:
    def __init__(self):
        self.Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.System_Host_Name = socket.gethostname()
        self.System_IP_Address = socket.gethostbyname(self.System_Host_Name)
        self.Interface_Port = 9999
        self.Server_Socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.Server_Socket.bind((self.System_IP_Address,self.Interface_Port))
        self.Server_Socket.listen()
        self.Break_Socket_connections = False
    
    def Accept_client_request(self):
        print(f"server Ip : {self.System_IP_Address} Server port : {self.Interface_Port}")
        print("Waiting for connection.....")
        self.Client_Socket,self.Client_address = self.Server_Socket.accept()
        print(f"Conneted with : {self.Client_address} ")
        data = str(self.Client_Socket.recv(1024).decode())
        print(data)
        self.Response_manager()
    
    def Response_manager(self):
        target = self.Client_Socket
        while True:
            i = input("Enter your message : ")
            send_data = pickle.dumps({"Notifier": i})
            send_data = bytes(f'{len(send_data):{10}}',"utf-8")+send_data
            target.send(send_data)


if __name__== "__main__":
    chatApp = Chat_Application()
    chatApp.Accept_client_request()