import numpy as np
from sympy import numer
from CANMessage import CANMessage
from FunctionLibrary import createCANMessagesFromFile

filename = 'Log File Test/light_board_signal_1.log'
messagesToTarget = ['0x360', '0x361', '0x362', '0x363', '0x364', '0x365', '0x366', '0x367']

CANMessages = createCANMessagesFromFile(filename)

#CANMessages now stores a list of CANMessage objects, which includes data like the message ID, time it was received and the hexidecimal data itself. Could now theoretically filter for specific IDs


#print(CANMessages)

FilteredCANList = []
numberOfOccurances = np.zeros(len(messagesToTarget))
for message in CANMessages:
    if message.CANMessageID in messagesToTarget:
        FilteredCANList.append(message)

print(FilteredCANList)

for message in FilteredCANList:
    for i,id in enumerate(messagesToTarget):
        if message.CANMessageID == id:
            numberOfOccurances[i] += 1

print(numberOfOccurances)