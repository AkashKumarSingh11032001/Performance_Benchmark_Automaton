from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from os.path import dirname

 

def identifyCtrl(server, user, passd, dirx):
    localPath= dirname(__file__)
    
    loc = "{0}\\logs\\ctrl_res.txt".format(localPath)
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