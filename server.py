import socketserver
import handler

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), handler.MyTCPHandler)

    server.serve_forever()
