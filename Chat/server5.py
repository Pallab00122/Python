import socket
import threading

clients = {}  # {conn: username}

def broadcast_client_list():
    """Send updated user lists to all clients, excluding themselves."""
    for conn, username in clients.items():
        try:
            # Exclude self from the list
            other_users = [u for u in clients.values() if u != username]
            message = "USERLIST:" + ",".join(other_users)
            conn.send(message.encode())
        except:
            pass

def send_private(sender_conn, recipient_name, message):
    """Send a message only to the recipient (private)."""
    sender_name = clients.get(sender_conn, "Unknown")
    for conn, uname in clients.items():
        if uname == recipient_name:
            try:
                conn.send(f" {sender_name} -> {message}".encode())
            except:
                pass
            break
    # else:
    #     # Recipient not found → notify sender only
    #     try:
    #         sender_conn.send(f"❌ User '{recipient_name}' not found.".encode())
    #     except:
    #         pass

def handle_client(conn, addr):
    try:
        username = conn.recv(1024).decode()
        clients[conn] = username
        print(f"{username} connected from {addr}")

        broadcast_client_list()

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            try:
                recipient, message = data.split("|", 1)
                send_private(conn, recipient, message)
            except ValueError:
                # If format wrong → ignore or log
                pass
    except:
        pass
    finally:
        print(f"{clients.get(conn, addr)} disconnected")
        left_user = clients.pop(conn, None)
        conn.close()
        broadcast_client_list()
        if left_user:
            # Notify all remaining users
            for c in clients:
                try:
                    c.send(f" {left_user} left the chat".encode())
                except:
                    pass


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print("✅ Server started. Waiting for connections...")
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
