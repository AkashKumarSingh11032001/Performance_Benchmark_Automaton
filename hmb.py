from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer


def HmbOnOff(server, user, passd, dirx):
    # Reboot the server
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="reboot",
    )
    # sleep for 60 seconds, inorder to bring system up.
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="nvme set-feature /dev/nvme0 -f 0x0d -v 0x00",
    )
