from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def HmbOnOff(server, user, passd, dirx):
    # HostsConnectionandCommandExecution(
    #     server=server,
    #     username=user,
    #     password=passd,
    #     directoryx=dirx,
    #     commandx="reboot",
    # )
    
    # print("Wait for reboot and restablishing the connection: ")
    # print("Waiting Time Left: ")
    # countdown(71)
    # print("\nConnection Established!\n")
        
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="nvme set-feature /dev/nvme0 -f 0x0d -v 0x00",
    )
    
    print("HMB Turned OFF Successfully!!\n")
