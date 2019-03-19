import socket, time, threading, sys, pymongo
from multiprocessing import Process
from MongoDB import Database
db = Database()
rooms = []

class Room:
    def __init__(self, roomId):
        self.roomId = roomId
        self.connections = []
    def sendMsg(self, msg):
        print('sending message: '+msg)
        for i in range(len(self.connections)):
            try:
                msg = msg + '\n'
                self.connections[i].send(msg.encode())
            except:
                print('error sending msg')
    def addCon(self, con):
        self.connections.append(con)
        #self.sendMsg("Client has connected.");

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
            print('action: '+self.action)
            if self.action == 'newRoom':
                room = Room(self.username)
                rooms.append(room)
                self.connectToRoom(self.username)
            if self.action == 'connectToRoom':
                self.connectToRoom(self.recvMsg())
            if self.action == 'record':
                locallist = db.getData()
                try:
                    line = str(locallist[0][self.username]) + '\n'
                except:
                    line = 'Error getting values!\n'

                print(line)
                self.client.send(line.encode())
        else:
            print('failed :(')
            
        print('closing connection...')
        self.client.close()

class Server:
    def __init__(self, port):
        while True:
            try:
                self.port = port
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
    def close(self):
        self.socket.close()
        
def commands():
    while True:
        command = input()
        if command == 'getRooms':
            print(rooms)
        if command == 'sendAll':
            for i in range(len(rooms)):
                rooms[i].sendMsg(input('enter msg to send'))
        if command == 'clearRooms':
            print('cleared')
        if command == 'end':
            print('trying to end')
            server.close()
            sys.exit()
        if command == 'getData':
            locallist = db.getData()
            print(locallist[0])

threading.Thread(target=commands).start()

server = Server(4545)
try:    
    server.listen()
except:
    server.close()
