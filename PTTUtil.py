import sys
import time
from time import gmtime, strftime

def Log(InputMessage):
    TotalMessage = "[" + strftime("%Y-%m-%d %H:%M:%S") + "]" + InputMessage
    #text.encode(sys.stdout.encoding)
    #print(TotalMessage.encode('utf-8-sig', 'ignore').decode('utf-8-sig'))
    print(TotalMessage.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
    #
def getTime():
    return strftime("%H:%M")

def readPostFile(FileName):
    result = ''
    try:
        with open(FileName, encoding = 'utf-8-sig') as File:
            Temp = File.readlines()
            Temp = [x.strip() for x in Temp]
            result = '\r\n'.join(Temp)
    except FileNotFoundError:
        return None
    return result
