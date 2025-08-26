import socket

if __name__ == "__main__":
    host='127.0.0.1'
    port=12345

    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)
    print("Server is running and wait for connection")
    conn,addr=server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data=conn.recv(1024).decode()
        if not data:
            print(f"Connection lost ...")
            break
        print(f"Received from cliend data : {data}")

    conn.close()
    server_socket.close()
    