# udp_gb_server.py
'''服务端（UDP协议局域网广播）'''
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 9999
while 1:
    time.sleep(5)
    network = '<broadcast>'
    s.sendto('I am blind not deaf!'.encode('utf-8'), (network, PORT))
