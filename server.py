import socket

def encode_number(n):
    powers = [81, 27, 9, 3, 1]
    from itertools import product
    for coeffs in product([-1, 0, 1], repeat=5):
        value = sum(c * p for c, p in zip(coeffs, powers))
        if value == n:
            return coeffs
    return None

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Server is running... Waiting for client.")

conn, addr = s.accept()
print("Connected with client")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        break
    n = int(data)
    code = encode_number(n)
    if code:
        conn.send(str(code).encode())
    else:
        conn.send("Invalid input".encode())

conn.close()
s.close()
