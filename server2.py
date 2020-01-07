import socket
import threading
from .commands import Worker

def run(self):
        """
        run the server
        """
        self.initialize()
        while True:
            for conn, address in zip(self.connections, self.ips):
                try:
                    if not self.threads[address]:
                        threading.Thread(target=self.respond, args=(conn, address), daemon=True).start()
                except:
                    pass

    def respond(self, conn, addr):
        """respond to every connected client"""
        try:
            self.threads[addr] = True
            client_res = str(conn.recv(4096), "utf-8")
            response = self.workers[addr].execute(client_res)
            encoded_str = str.encode(response)
            conn.send(encoded_str)
            self.threads[addr] = False
        except Exception as exps:
            print(exps)