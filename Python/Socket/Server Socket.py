import socket
port = 42069
HOST = ""
with socket.socket(socket.AF_INET) as s:
    s.bind((HOST,port))
    s.listen(1)
    connection,address = s.accept()
    with connection:
        print("Connected by: " + str(address))
        x = True
        while x:
            data = connection.recv(1024)
            if not data:
                break
            else:  
                if data == b"Client has closed connection.":
                    print(repr(data))
                    connection.close()
                    break      
                print("Client: " + str(data))
                msgback = input("Message to client: \n")
                if msgback == "close":
                    msgback = "Server has closed connection."
                    connection.sendall(msgback.encode("utf-8"))
                    connection.close()
                    break
                connection.sendall(msgback.encode("utf-8"))