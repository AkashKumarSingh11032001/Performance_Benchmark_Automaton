import os
import paramiko

host = "10.207.48.182"
user = "qa"
passd = '12'

ssh = paramiko.SSHClient() 
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=passd)
sftp = ssh.open_sftp()
sftp.put("text.txt", "text.txt") # copy file from host to remote
sftp.get("text.txt", "text.txt") # copy file from remote to host
sftp.close()
ssh.close()