import socket
import struct


def ip_to_int(ip_string):
    return struct.unpack("!I", socket.inet_aton(ip_string))[0]


def int_to_ip(ip_int):
    return socket.inet_ntoa(struct.pack("!I", ip_int))


if __name__ == '__main__':
    print ip_to_int('180.119.68.159')
    print int_to_ip(3027715231)
