from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer


def bpc1(server, user, passd, dirx, doc):
    locFile = doc
    HostsFileTransfer(
        server=server,
        username=user,
        password=passd,
        localFileNameWithLocation=locFile,
        remoteFileNameWithLocation=f"/root/test/a.txt",  # /home/qa/test/preCondition/bpc0.sh",
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
        localFileNameWithLocation="Performance_Benchmark_Automaton/logs/res.log",
        remoteFileNameWithLocation="/root/test/res.log",
        copyToServer=False,
    )
