#coding=utf-8
 
from socket import *
import time

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
 
# 2. 准备接收方的地址
# '47.114.93.195'表示目的ip地址
# 22表示目的端口
dest_addr = ('47.114.93.195', 22)  # 注意 是元组，ip是字符串，端口是数字
 
# 3. 从本地读取数据
f = open("data", "r")
send_data = f.read()
f.close()

# 4. 发送数据到指定的电脑上的指定程序中
'''
volume_list = [v for v in range(10, 35, 5)]
for v in volume_list:
    for i in range(2 ** v):
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        time.sleep(120)
'''
packet_count = 0
now = 0
time_begin = time.time()
while True:
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    packet_count += 1
    if (time.time() - time_begin) // 60 > now:
        print("Bandwidth: %.6f Mbps" % ((packet_count * len(send_data) * 8) / (time.time() - time_begin) / (2 ** 20)))
        now += 1

# 5. 关闭套接字
udp_socket.close()
