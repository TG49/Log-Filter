from CANMessage import CANMessage
def readData(filename, access='r'):
    """Read data out of a file"""
    file = open(filename, access)
    data = file.readlines()
    file.close()
    return data

def beginningEndPositionsOfByteData(data):
    """Take a list of data lines and output the indexes of the bytedata as tuples"""
    first = []
    second = []
    FLAGNODASH = 0
    FLAGEXTRADASH=0
    for i, line in enumerate(data):
        if i == 0:
            continue
        if FLAGNODASH == 1:
            if '----' in data[i+1].split():
                FLAGNODASH = 0
            continue
        if FLAGEXTRADASH ==1:
            if 'Elapsed' in line.split() or 'ms' in line.split():
                FLAGEXTRADASH = 0
            continue
        if (i+4)<(len(data)+1):
            if '----' in line.split():
                for j in range(2,20):
                    if ('----' in data[i+j].split()):
                        FLAGEXTRADASH=1
                        break
                    elif 'Elapsed' in data[i+j].split() or 'ms' in data[i+j].split():
                        first.append(i+1)
                        break
                continue
            if 'Elapsed' in line.split() or 'ms' in line.split():
                second.append(i-1)
                if '----' not in data[i+2].split():
                    FLAGNODASH = 1
    return list(zip(first, second)) #contains list of tuples with the index of the beginning and end of the data stored


def createCANMessageList(bytedata, data):
    """Take indexes of byte data and create a list of CANMessages"""
    CANMessages = []
    for byteDatum in bytedata:
        try:
            time = int(data[byteDatum[0]-3].split()[2])
        except:
            time = None
        
        try:
            CANMessageID = data[byteDatum[0]-2].split()[2]
        except:
            CANMessageID=None
        
        try:
            individualCANMessageData = [data[i].split()[0] for i in range(byteDatum[0], byteDatum[1])]
        except:
            individualCANMessageData = None
        CANMessages.append(CANMessage(CANMessageID, time, individualCANMessageData))
    return CANMessages

def createCANMessagesFromFile(filename, access='r'):
    """Creates a list of CANMessage objects based on the input log file"""
    data = readData(filename, access)
    byteData = beginningEndPositionsOfByteData(data)
    CANMessages = createCANMessageList(byteData, data)

    return CANMessages
