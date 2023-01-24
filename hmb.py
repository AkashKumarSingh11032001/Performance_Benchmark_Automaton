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
    # Reboot the server
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="reboot",
    )
    
    # sleep for 60 seconds, inorder to bring system up.
    # time.sleep(70)
    print("Wait for reboot and restablishing the connection: ")
    print("Waiting Time Left: ")
    countdown(71)
    print("\nConnection Established!\n")
    print("HMB Turned OFF Successfully!!\n")
        
    # Restablish the connection and execute cmd for HMB-OFF
    HostsConnectionandCommandExecution(
        server=server,
        username=user,
        password=passd,
        directoryx=dirx,
        commandx="nvme set-feature /dev/nvme0 -f 0x0d -v 0x00",
        # commandx="echo Hello World!",    
    )
    
