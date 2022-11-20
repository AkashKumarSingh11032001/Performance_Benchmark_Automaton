from pypsexec.client import Client
import os
import time
import sys
import spur
import paramiko

server = "10.207.48.182"
user = "qa"
passd = "12"

# <-----------connection 1----------->
# shell = spur.SshShell(hostname=host, username=user, password=passd,missing_host_key=spur.ssh.MissingHostKey.accept)
# result = shell.run(["ls"])
# # result = shell.run(["echo", "-n", "hello"])
# print (result.output) # prints hello

# <-----------connection 2----------->
# client = paramiko.SSHClient()
# client.load_system_host_keys()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname=server, username=user, password=passd)

# # change directory to the location of where you want to run the command and
# dirt = "/home/qa/test"
# command = "echo Hello"  # change command to the command you want to execute

# _stdin, _stdout, _stderr = client.exec_command(f'cd {dirt}; {command}')
# print(_stdout.read().decode())
# client.close()

# sftp = ssh.open_sftp()
# sftp.put("text.txt", "text.txt") # copy file from host to remote
# sftp.get("text.txt", "text2.txt") # copy file from remote to host
# sftp.close()
# ssh.close()


def HostsConnection(hostname=server, username=user, password=passd, directory=dirx, command=cmd):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=server, username=user, password=passd)

    directory = dirx  # change directory to the location of where you want to run the command and
    command = cmd  # change command to the command you want to execute

    _stdin, _stdout, _stderr = client.exec_command(
        f'cd {directory}; {command}')
    print(_stdout.read().decode())
    client.close()


def HostsFileTransfer(hostname=server, username=user, password=passd, localFileNameWithLoaction=local, remoteFileNameWithLoaction=remote, copyToServer=True):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=server, username=user, password=passd)

    sftp = client.open_sftp()
    if copyToServer:
        # copy file from host to remote -> copyToServer
        sftp.put(localFileNameWithLoaction, remoteFileNameWithLoaction)
    else:
        # copy file from remote to host
        sftp.get(remoteFileNameWithLoaction, localFileNameWithLoaction)

    sftp.close()
    client.close()
