import socket

def whois_lookup(domain: str) -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.iana.org", 43))
        s.send(f"{domain}\r\n".encode())

        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data

        s.close()
        return response.decode().strip()

    except socket.error as e:
        return f"Error: {str(e)}"

print(whois_lookup("example.com"))