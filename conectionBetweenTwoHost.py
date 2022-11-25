from pypsexec.client import Client
import os
import time
import sys
import spur
import paramiko


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


def RemoteSudo(client):
    client.exec_command("sudo -i")


def StreamOutput(output):
    line_buf = b""
    while not output.channel.exit_status_ready():
        line_buf += output.read(1)
        if line_buf.endswith(b"\n"):
            yield line_buf
            line_buf = b""


def HostsConnectionandCommandExecution(
    server, username, password, directoryx, commandx
):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.get_transport()
    client.connect(hostname=server, username=username, password=password)

    directory = directoryx  # change directory to the location of where you want to run the command and
    command = commandx  # change command to the command you want to execute

    _stdin, _stdout, _stderr = client.exec_command(f"cd {directory}; {command}")

    for l in StreamOutput(_stdout):
        print(l.decode("utf-8"))
    # return _stdout.read().decode()
    client.close()


def HostsFileTransfer(
    server,
    username,
    password,
    localFileNameWithLocation,
    remoteFileNameWithLocation,
    copyToServer=True,
):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.get_transport()
    client.connect(hostname=server, username=username, password=password)
    sftp = client.open_sftp()

    # cmd = "sudo su"
    # _stdin,_stdout,_stderr = client.exec_command(command=cmd)
    # _stdin.write("12\n")

    if copyToServer:
        # copy file from host to remote -> copyToServer = True
        sftp.put(localFileNameWithLocation, remoteFileNameWithLocation)
    else:
        # copy file from remote to host -> copyToServer = False
        sftp.get(remoteFileNameWithLocation, localFileNameWithLocation)

    sftp.close()
    client.close()
