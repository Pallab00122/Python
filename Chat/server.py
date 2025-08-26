import socket
import threading

clients=[]  # Store all the connected client sockets

def handle_client(conn,addr):
    print(f"New connection from {addr}")
    while True:
        try:
            data=conn.recv(1024).decode()
            if not data:
                print(f"{addr} disconnected")
                clients.remove(conn)
                break
            else:
                print(f"Received from {addr}: {data}")
        except:
            continue
    conn.close()

"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message,sender_conn=None):  #message → The text you want to send to all clients.
    # sender_conn → The socket of the client who sent the message
    for client in clients:
        if client !=sender_conn:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)    

# Allow server admin to type and send messages
def server_input():
    message=input("server :")
    broadcast(f"Server : {message}")


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12345

    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen()
    print("server started waiting for connection ")

    threading.Thread(target=server_input, daemon=True).start()
    
    while True:
        conn,addr=server_socket.accept()
        clients.append(conn)
        """Maintains a list of clients for ease of broadcasting 
           a message to all available people in the chatroom"""
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
