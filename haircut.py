import json
import datetime


database ='F:\CODING\PYTHON\PROJECTS\haircut\\haircut.json'

def loaddata():
    with open(database,'r') as f :
        data= json.load(f)
    return data

def writedata(database,data):
    with open(database,'w') as f:
        json.dump(data,f,indent=4)


def meanu():
    code=None
    print(" MEANU           CODE\n")
    print("records          [0]")
    print("entry            [1]")
    print("statistics       [2]")
    code = int(input("\nEnter CODE : "))
    return code

def entry():
    user="SID"
    currtime = str(datetime.datetime.now())
    data = loaddata()
    data[user]["datetime"].append(currtime)
    writedata(database,data)
    print(f"entry for {currtime} sucessesfully done.")
        
def record():
    user = 'SID'
    data=loaddata()
    entrys = data[user]["datetime"]
    for entry in entrys:
        print(entry)


if __name__ == '__main__':
    # this is how SWITCH statement will be used in PYTHON

    code = meanu() 
    if code == 0:
        record()
    elif code == 1:
        entry()
    else:
        print("Invalid code! Please try to enter valid code,")
        meanu()
  

        
    
