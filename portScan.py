import socket # for socket
import sys
import argparse


parser = argparse.ArgumentParser(description="Parse IP and Ports")

parser.add_argument('ip_address',type=str,help='IP_address of the target to be scanned')

parser.add_argument('fst_port',type=int, help="The first port where port scan will start")

parser.add_argument('lst_port',type=int, help='Till the port you want to scan')

args = parser.parse_args()

Ip_offset = args.ip_address

first_port = args.fst_port

last_port = args.lst_port

for i in range(first_port,last_port +1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))
    
    # default port for socket
    #port1 = 80
    #port2 = 443

    host_ip = Ip_offset
    
    # connecting to the server
    try:
        s.connect((host_ip, i))
        print(f"CONGRATULATIONS ! You have discovered an open port successfully of {Ip_offset} at port {i}")
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created again ")

    except TimeoutError:

        print(f"there was an error connecting to port {i} for {host_ip}")

    except ConnectionRefusedError:

        print(f"{host_ip} refuted the connection actively on port {i}")

    except OSError:

        print(f"{OSError}")