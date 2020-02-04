from flask import Flask
from flask import jsonify
from socket import *

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)


@app.route('/try')
def my_try(client_socket):

    """为一个客户端服务"""
    # 接收对方发送的数据
    recv_data = client_socket.recv(1024).decode("utf-8") #  1024表示本次接收的最大字节数
    # 打印从客户端发送过来的数据内容
    #print("client_recv:",recv_data)
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)
     
    # 返回浏览器数据
    # 设置返回的头信息 header
    #response_headers = "HTTP/1.1 200 OK\r\n" # 200 表示找到这个资源
    #response_headers += "\r\n" # 空一行与body隔开
    # 设置内容body
#    response_body = "<h1>fat boss<h1>\r\n" 
#    response_body += "<h2>come on<h2>\r\n" 
#    response_body += "<h3>binlang!!!<h3>\r\n" 

    # 合并返回的response数据
#    response = response_headers + response_body

    # 读取html文件内容
    file_name = "demo.html" # 设置读取的文件路径
    f = open(file_name,"rb") # 以二进制读取文件内容
    response_body = f.read()
    f.close()

    # 返回数据给浏览器
    client_socket.send(response_headers.encode("utf-8"))   #转码utf-8并send数据到浏览器
    client_socket.send(response_body)   #转码utf-8并send数据到浏览器
    client_socket.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
