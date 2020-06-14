"""
@File : client.py

@Author: sivan Wu

@Date : 2020/6/13 8:22 下午

@Desc :

"""

import socket
# 1. 创建一个套接字对象
sk = socket.socket()
# 2. 连接服务端, 必须是服务端的ip地址以及端口
sk.connect(("127.0.0.1", 9001))
# 3. 接收server端传来的数据，因为server端中首先发送数据
data = sk.recv(1024)
print(data)
# 4. 发送数据给服务端，因为server端中发送数据之后会接收数据
sk.send(b"i am client")
# 5. 关闭
sk.close()
