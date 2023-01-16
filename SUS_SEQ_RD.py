from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from os.path import dirname

def sus_seqrd(server, user, passd, dirx, doc):
    
    localPath= dirname(__file__)
    locFile = doc
    
    HostsFileTransfer(
        server=server,
        username=user,
        password=passd,
        localFileNameWithLocation=locFile,
        remoteFileNameWithLocation=f"/root/fio/a.txt",  # /home/qa/test/preCondition/bpc0.sh",
    )
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="chmod -R 777 a.txt",
    )
    
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="fio a.txt --eta-newline=1 --eta=always | tee res.log",
    )

    HostsFileTransfer(
        server=server,
        username=user,
        password=passd,
        localFileNameWithLocation="{0}\\logs\\sus_seqrd.log".format(localPath),
        remoteFileNameWithLocation="/root/fio/res.log",
        copyToServer=False,
    )
