class CANMessage:
    """CANMessage Data class"""
    def __init__(self, CANMessageID, Time, Data):

        self.CANMessageID = CANMessageID
        self.Time = Time
        self.Data = Data


    def __repr__(self):
        d = "\nCANMessage     {}\n".format(self.CANMessageID)
        d += "Time:            {}\n".format(self.Time)
        d += "Data:    {}\n".format(self.Data)
        return d
