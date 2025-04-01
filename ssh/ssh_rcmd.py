import paramiko
import getpass
import shlex
import subprocess

def ssh_command(ip, port, user, pwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=port, username=user, password=pwd)
    
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(cmd)
        print(ssh_session.recv(1024).decode())
        while True:
            cmd = ssh_session.recv(1024)
            try:
                d_cmd = cmd.decode()
                if d_cmd == 'exit':
                    client.close()
                    break
                cmd_output = subprocess.check_output(shlex.split(d_cmd), shell=True)
                ssh_session.send(cmd_output or 'okay')
            except Exception as e:
                ssh_session.send(str(e))
            client.close()
    return

if __name__ == '__main__':
    # user = getpass.getuser() # Get the username from the environment
    user = input('Enter username: ')
    pwd = getpass.getpass()
    
    ip = input('Enter server IP: ')
    port = input('Enter server port: ')
    cmd = input('Enter command to run: ')
    
    ssh_command(ip=ip, port=port, user=user, pwd=pwd, cmd='Client Connected')