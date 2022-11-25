from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from BPC0 import bpc0



server = "10.207.48.244"  # "10.207.48.182"
user = "qa"
passd = "12"

dirx = "/home/qa/test/"


HostsFileTransfer(
    server=server,
    username=user,
    password=passd,
    localFileNameWithLocation=x[0],
    remoteFileNameWithLocation="/home/qa/test/a.txt",  # /home/qa/test/preCondition/bpc0.sh",
)

HostsConnectionandCommandExecution(
    server=server,
    username=user,
    password=passd,
    directoryx=dirx,
    commandx="chmod -R 777 a.txt",
)
x = HostsConnectionandCommandExecution(
    server=server,
    username=user,
    password=passd,
    directoryx=dirx,
    commandx="./a.txt",
)
print(x)