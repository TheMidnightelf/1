import socket
HOST = "localhost"
port = 42069
x = True
with socket.socket(socket.AF_INET) as s:
    s.connect((HOST,port))
    print("Connected to server!")
    while x:
        msg = str(input("Message to server: \n"))
        if msg == "close":
            msg = "Client has closed connection."
            s.sendall(msg.encode("utf-8"))
            s.close()
            break
        s.sendall(msg.encode("utf-8"))
        data = s.recv(1024)
        if data == b"Server has closed connection.":
            print(repr(data))
            s.close()
            break
        print("Server: " + repr(data))