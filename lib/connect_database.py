import pymysql
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(
    ("118.178.58.86",22),
    ssh_password = 'Lsxd3@110624',
    ssh_username = 'root',
    remote_bind_address = ('127.0.0.1',3307)) as sever:

    db_connect = pymysql.connect(host = '127.0.0.1',
                                 port = sever.local_bind_port,
                                 user = 'root',
                                 password = 'lhb767',
                                 db = 'new_sys')