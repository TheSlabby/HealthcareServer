import socket, threading, time, sys

rooms = []

class Room:
    def __init__(self, roomId):
        self.roomId = roomId
        self.connections = []
    def sendMsg(self, msg):
        print('sending message: '+msg)
        for i in range(len(self.connections)):
            try:
                self.connections[i].send(msg.encode())
            except:
                print('error sending msg')
    def addCon(self, con):
        self.connections.append(con)

class Connection:
    def __init__(self,client,address, server):
        self.client = client
        self.address = address
        self.server = server
    
    def recvMsg(self):
        try:
            data = self.client.recv(1024)
        except:
            return False
        if data:
            return data.decode().strip()
        else:
            return False
    
    def connectToRoom(self,roomId):
        self.connectedRoom = False
        for i in range(len(rooms)):
            if rooms[i].roomId == roomId:
                self.connectedRoom = rooms[i]
                
                #loop for sending and receiving messages
        if self.connectedRoom != False:
            self.connectedRoom.addCon(self.client)
            while True:
                msgToSend = self.recvMsg()
                if msgToSend != False:
                    msgToSend = self.type + ' ' + self.username + ' > ' + msgToSend
                    self.connectedRoom.sendMsg(msgToSend)
                else:
                    print('connection died!')
                    break
        else:
            print('didnt find a room!')
    
    def start(self):
        self.username = self.recvMsg()
        self.type = self.recvMsg()
        self.action = self.recvMsg()
        
        if self.username != False and self.type != False and self.action != False:
            print('success' + self.username)
            
            if self.action == 'newRoom':
                room = Room(self.username)
                rooms.append(room)
                self.connectToRoom(self.username)
            if self.action == 'connectToRoom':
                self.connectToRoom(self.recvMsg())
        else:
            print('failed :(')
            
        print('closing connection...')
        self.client.close()

class Server:
    def __init__(self, port):
        while True:
            print('server created')
            try:
                self.port = port
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.bind(('',port))
                print('successfully binded!')
                break
            except:
                print('error binding, retrying...')
                time.sleep(5)
    def listen(self):
        self.socket.listen(5)
        while True:
            client, address = self.socket.accept()
            connection = Connection(client, address, self)
            threading.Thread(target = connection.start).start()

def commands():
    while True:
        command = input()
        if command == 'getRooms':
            print(rooms)
        if command == 'sendAll':
            for i in range(len(rooms)):
                rooms[i].sendMsg(input('enter msg to send'))

threading.Thread(target=commands).start()
server = Server(4545)
server.listen()
