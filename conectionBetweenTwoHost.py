from pypsexec.client import Client
import os
import time
import sys
import spur
import paramiko

host = "10.207.48.182"
user = "qa"
passd = '12'


shell = spur.SshShell(hostname=host, username=user, password=passd,missing_host_key=spur.ssh.MissingHostKey.accept)
result = shell.run(["ls"])
# result = shell.run(["echo", "-n", "hello"])
print (result.output) # prints hello
