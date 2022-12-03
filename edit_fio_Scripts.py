from csv import writer
from pathlib import Path
 
def ScriptFIO():
    # assign directory
    directory = f'fioScripts'
    preConditionData = f'Scriptdata.txt'
    
    FIOFiles = []
    files = Path(directory).glob('*')
    for file in files:
        FIOFiles.append(file)

    # print(FIOFiles) 

    # # Heading
    mylines = []
    # print(FIOFiles)
    with open(file) as fp:
        for x in fp:
            mylines.append(x)   

    heading = []
    for i in range(2, len(mylines)):
        x = mylines[i].split('=')
        if(len(x) == 2):
            heading.append(x[0])

    with open(preConditionData, 'w') as f_object:
        f_object.write(str(heading)+ "\n")  


    # print("Heading Data => {0}".format(heading))    


    # # Values
    for lisx in FIOFiles:
        mylines = []
        with open(lisx) as fp:
            for x in fp:
                mylines.append(x)

        value = []
        for i in range(2, len(mylines)):
            x = mylines[i].split('=')
            if(len(x) == 2):
                value.append(x[1][:len(x[1])-1])    

        # print("Values Data => {0}".format(value))

        with open(preConditionData, 'a') as f_object:
            f_object.write(str(value)+ "\n")
            
def BPC():
    # assign directory
    directory = f'BPCFile'
    preConditionData = f'bpcdata.txt'
    
    FIOFiles = []
    files = Path(directory).glob('*')
    for file in files:
        FIOFiles.append(file)   

    # print(FIOFiles) 

    # Heading
    mylines = []
    with open(file) as fp:
        for x in fp:
            mylines.append(x)   

    heading = []
    for i in range(2, len(mylines)):
        x = mylines[i].split('=')
        if(len(x) == 2):
            heading.append(x[0])
            
    with open(preConditionData, 'w') as f_object:
        f_object.write(str(heading)+ "\n")  
    

    # print("Heading Data => {0}".format(heading))    
    

    # Values
    for lisx in FIOFiles:
        mylines = []
        with open(lisx) as fp:
            for x in fp:
                mylines.append(x)
        
        value = []
        for i in range(2, len(mylines)):
            x = mylines[i].split('=')
            if(len(x) == 2):
                value.append(x[1][:len(x[1])-1])    

        # print("Values Data => {0}".format(value))
        
        with open(preConditionData, 'a') as f_object:
            f_object.write(str(value)+ "\n")
            

# BPC()
ScriptFIO()
print("----------------> Task Completed!!!")
    