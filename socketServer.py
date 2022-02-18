import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            dataReceived = self.request.recv(20)
            if not dataReceived: break
            self.request.send(dataReceived)

myServer = socketserver.ThreadingTCPServer(('',8888), MyHandler)
myServer.serve_forever(  )

#
