import socket
import threading

clients={}

def broadcast_client_list():
    for conn,username in clients.items():
        try:
            other_users=[u for u in clients.values() if u != username]   # [u for u in ["Riya", "Akash", "Puja"] if u != "Akash"]
            message = "USERLIST:" + ",".join(other_users)
            conn.send(message.encode())
        except:
            pass

def send_private(sender_conn, recipient_name, message): # recipient_name → jake message pathate hobe (username ) sender_conn → je user message pathacche, tar connection (socket).
    sender_name=clients.get(sender_conn)
    for conn,uname in clients.items():
        if uname == recipient_name:  #(key,value => conn = conn1, uname = "PK")
            try:
                conn.send(f"{sender_name} -> {message}".encode())
            except:
                pass
            break

def handle_client(conn, addr):
    try:
        username=conn.recv(1024).decode() # In the first client just send the user name(PK) ,means 
        clients[conn]=username
        print(f"{username} connected from {addr}")  # PK connected from 4777

        broadcast_client_list()

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            try:
                recipient, message=data.split("|" , 1) #   Akash|Hello" → split recipient = "Akash", message = "Hello"
                # full_message = f"{username} → {recipient}: {message}"
                send_private(conn, recipient, message)
            except ValueError:
                # full_message = f"{username}: {data}"
                pass

    except:
        pass
    finally:
        print(f"{clients.get(conn, addr)} disconnected")
        left_user = clients.pop(conn, None)
        conn.close()
        broadcast_client_list()
        if left_user:
            for c in clients:
                try:
                    c.send(f"{left_user} left the chat ")
                except:
                    pass
        

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12345

    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen()
    # server_socket.settimeout(60.0)

    print(" Server started. Waiting for connections...")
    while True:
        conn,addr=server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
