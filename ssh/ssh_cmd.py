import paramiko
import getpass

def ssh_command(ip, port, user, pwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=port, username=user, password=pwd)
    
    _, stdout, stderr = client.exec_command(command=cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('----OUTPUT----')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    # user = getpass.getuser() # Get the username from the environment
    user = input('Enter username: ')
    pwd = getpass.getpass()
    
    ip = input('Enter server IP: ')
    port = input('Enter server port: ')
    cmd = input('Enter command to run: ')
    
    ssh_command(ip=ip, port=port, user=user, pwd=pwd, cmd=cmd)