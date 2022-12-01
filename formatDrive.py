from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer


def driveFormat(server, user, passd, dirx):
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="nvme format /dev/nvme0 --namespace-id=1 , -n 1",
    )
