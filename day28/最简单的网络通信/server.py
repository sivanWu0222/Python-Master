"""
@File : socket.py

@Author: sivan Wu

@Date : 2020/6/13 8:22 下午

@Desc :

"""

import socket

# 1. 实例化一个socket模块中socket类的对象
sk = socket.socket()
# 2. 服务端绑一个地址(本机地址或自己的ip地址)以及端口，因为别人要找你
# 传入的参数是一个元祖，第一个是字符串类型，代表ip地址，第二个是整形，代表端口
sk.bind(("127.0.0.1", 9001))
# 3. 开启监听，等待别人连接
sk.listen()
# 4. 接收客户端的连接，连上之后会返回一个连接以及地址(包括对面的ip地址以及端口)
conn, address = sk.accept()
print(address)
# 5. 我们和他说话使用send(),传入的只能是字节类型的数据，
conn.send(b"hello")
# 6. 他和咱们说话使用recv
msg = conn.recv(1024)  # 接收1024个字节的数据，如果超过也只接受1024个
print(msg)
# 7. 结束对话
conn.close()
# 8. 关掉服务
sk.close()
