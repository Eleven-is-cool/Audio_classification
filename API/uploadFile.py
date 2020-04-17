import sys
import paramiko  # 用于调用scp命令
from scp import SCPClient


# 将指定目录的图片文件上传到服务器指定目录
# remote_path远程服务器目录
# file_path本地文件夹路径
# img_name是file_path本地文件夹路径下面的文件名称
def upload_img(local_path):
    remote_path = "/usr/demo/file"
    host = "***.***.***.***"  # 服务器ip地址
    port = 22  # 端口号
    username = "root"  # ssh 用户名
    password = ""  # 密码

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)

    try:
        scpclient.put(local_path, remote_path)
    except FileNotFoundError as e:
        print(e)
        return "系统找不到指定文件"
    else:
        return "文件上传成功"
    ssh_client.close()


if __name__ == '__main__':
    print(upload_img(sys.argv[1]))