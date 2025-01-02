import socket

def s(link):
    if link.startswith("https://"):
        return link[len("https://"):]
    elif link.startswith("http://"):
        return link[len("http://"):]
    else:
        return link

link = input('Enter your link: ')
link = s(link)

try:
    ip = socket.gethostbyname(link)
    print(f"Link: {link}\nIP: {ip}")
except socket.gaierror as e:
    print(f"Error: {e}")
