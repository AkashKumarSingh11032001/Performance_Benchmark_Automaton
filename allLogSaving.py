import os
import shutil
from os.path import dirname

localPath = dirname(__file__)


def logSaving(bpc, hmb, data_a, fileName, copyFrom):

    firmwareFolder = data_a[0]
    capacity = data_a[1]

    # create folder
    if bpc == "BPC0":
        if hmb == "HMB_ON":
            path = "{0}\\results\\{1}\\{2}\\{3}".format(
                localPath, firmwareFolder, capacity, "BPC0_HMB_ON")
        else:
            path = "{0}\\results\\{1}\\{2}\\{3}".format(
                localPath, firmwareFolder, capacity, "BPC0_HMB_OFF")
    elif bpc == "BPC1":
        if hmb == "HMB_ON":
            path = "{0}\\results\\{1}\\{2}\\{3}".format(
                localPath, firmwareFolder, capacity, "BPC1_HMB_ON")
        else:
            path = "{0}\\results\\{1}\\{2}\\{3}".format(
                localPath, firmwareFolder, capacity, "BPC1_HMB_OFF")

    # path = "{0}\\results\\{1}".format(localPath, firmwareFolder)
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)  # Create a new directory because it does not exist
        print("The new directory with {0}\{1} is created!".format(firmwareFolder,capacity))

    # copy file "original loc" to "target loc"
    fileName = "{0}_{1}_{2}.log".format(fileName, bpc, hmb)
    original = copyFrom
    target = "{0}\\{1}".format(path, fileName)
    shutil.copy(original, target)
