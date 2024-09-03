import socket # for socket
import sys

Ip_offset = '192.168.1.'

for i in range(0,256):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))
    
    # default port for socket
    port1 = 80
    port2 = 443
    i = str(i)
    ip_midwr = Ip_offset + i

    host_ip = ip_midwr
    
    # connecting to the server
    try:
        s.connect((host_ip, port1))
        print(f"Connected successfully with {host_ip} at port 80")
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created again ")

    except TimeoutError:

        print(f"there was an error connecting to port 80 for {host_ip}")

    except ConnectionRefusedError:

        print(f"{host_ip} refuted the connection actively")

    except OSError:

        print(f"{OSError}")

    

    try:
        s.connect((host_ip, port2))
        print(f" Connected successfully with {host_ip} at port 443")
    except TimeoutError:

        print(f"there was an error connecting to port 443 for {host_ip}")

    except ConnectionRefusedError:

        print(f"{host_ip} refuted the connection actively")

    except OSError:

        print(f"{OSError}")
    