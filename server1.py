import socket
import threading
from .commands import Worker

class Server():
    """server class for handling connections"""
    def __init__(self):
        self.s = None
        self.connections = self.create_empty("list")
        self.ips = self.create_empty("list")
        self.threads = self.create_empty("dict")
        self.workers = self.create_empty("dict")

    def create_empty(self, dtype):
        if dtype == "list":
            return []
        return {}

    def socket_job(self):
        """
        Create a socket and start accepting connections asyncronysly
        """
        try:
            self.s = socket.socket()
            self.s.bind(("", 8080))
            self.s.listen(5)
            print("Server opened at port 8080")
        except socket.error as msg:
            print("error: " + str(msg))
        while True:
            try:
                conn, address = self.s.accept()
                self.s.setblocking(1)
                self.connections.append(conn)
                self.ips.append(address)
                self.threads[address] = False
                # attach a worker to ip
                self.workers[address] = Worker(address)
                print("Client connected from ip :" + address[0])
            except:
                print("Error")

    def initialize(self):
        """
        initializing the socket job
        """
        try:
            threading.Thread(target=self.socket_job, args=(), daemon=True).start()
        except:
            print("Error in initializing")
