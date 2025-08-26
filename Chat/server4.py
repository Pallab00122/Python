import socket
import threading

clients = {}  # conn -> username

def broadcast(message):
    """Send a message to all connected clients."""
    for conn in clients:
        try:
            conn.send(message.encode())
        except:
            pass

def broadcast_client_list():
    """Send updated client list to all clients."""
    usernames = list(clients.values())
    message = "USERLIST:" + ",".join(usernames)
    for conn in clients:
        try:
            conn.send(message.encode())
        except:
            pass

def handle_client(conn, addr):
    try:
        # Receive username
        username = conn.recv(1024).decode()
        clients[conn] = username
        print(f"✅ {username} connected from {addr}")

        broadcast_client_list()
        broadcast(f"📢 {username} joined the chat")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            # Expect data as: "recipient|message"
            try:
                recipient, message = data.split("|", 1)
                full_message = f"{username} → {recipient}: {message}"
            except ValueError:
                full_message = f"{username}: {data}"  # Fallback

            broadcast(full_message)

    except:
        pass
    finally:
        print(f"❌ {clients.get(conn, addr)} disconnected")
        left_user = clients.pop(conn, None)
        conn.close()
        broadcast_client_list()
        if left_user:
            broadcast(f"📢 {left_user} left the chat")

def main():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print("🚀 Server started. Waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
