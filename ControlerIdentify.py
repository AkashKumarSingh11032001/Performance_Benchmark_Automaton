from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer

def identifyCtrl(server, user, passd, dirx):
    loc = "logs\\ctrl_res.txt"
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="rm controlerData.txt",
    ) 
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="nvme list >> controlerData.txt",
    )   
    HostsFileTransfer(
        server=server,
        username=user,
        password=passd,
        localFileNameWithLocation= loc,
        remoteFileNameWithLocation="/root/fio/controlerData.txt",
        copyToServer=False,
    )