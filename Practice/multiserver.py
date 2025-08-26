import socket
import threading


def handle_client(conn, addr):
    print(f"New connection {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                print(f"Conncetion with {addr} lost")
                break
            else:
                print(f"Received from {addr}: {data}")
        except ConnectionError:
            print(f"Connection reset by {addr}")
            break
    conn.close()


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    server_socket.settimeout(30.0)

    print("Server is running waiting for the connection")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
