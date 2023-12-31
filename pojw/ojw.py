import time
import socket
client = None
def millis():
    return round(time.time() * 1000.0)
class CTimer:
    nTimer                  = 0
    IsTimer                 = False
    def Set(self):
        self.IsTimer      = True
        self.nTimer       = millis()
    def Get(self):
        if self.IsTimer :
            return millis() - self.nTimer
        return 0
    def Destroy(self):
        self.IsTimer = False
def Connect():
    global client
    ip = '127.0.0.1'
    port = 5000
    client = socket.socket()
    client.connect((ip, port))
    print('connected')
def Disconnect():
    global client
    client.close()
def Send(*args):
    global m_nTime
    global m_nDelay
    global m_afMot
    global m_anIds

    argRes = change_to_numbers(*args)
    nIndex = 0
    if (is_all_numbers(*argRes) == True):
        if len(argRes) >= 2:
            strData = 's2'
            m_nTime = int(argRes[0])
            m_nDelay = int(argRes[1])
            m_afMot = []
            m_anIds = []
            for arg in argRes:
                nIndex = nIndex + 1
                strSep = ','
                bAngle = False
                if (nIndex > 2):
                    if ((nIndex % 2) == 0):
                        strSep = ':'
                        bAngle = True
                if (bAngle):
                    m_afMot.append(arg)
                    strData = strData + strSep + str(arg)
                else:
                    m_anIds.append(int(arg))
                    strData = strData + strSep + str(int(arg))
            client.send(b'\x02' + strData.encode('utf-8') + b'\x03')
def Send5(str):
    strData = 's5,1000,0,' + str
    print(strData)
    client.send(b'\x02' + strData.encode('utf-8') + b'\x03')
def is_all_numbers(*args):
    for item in args:
        if not isinstance(item, (int, float)):
            return False
    return True
m_nTime = 0
m_nDelay = 0
m_afMot = []
m_anIds = []
def change_to_numbers(*args):
    argRes = []
    for item in args:
        if not isinstance(item, (int, float)):
            item = item.replace(':', ',')
            items = item.split(',')
            for arg in items:
                argRes.append(float(arg))
        else :
            argRes.append(item)
    return argRes
# 1.0 == 100%를 의미
def wait_per(fPercent = -1.0):
    global m_nTime
    global m_nDelay
    nTime = 0
    nDelay = 0
    if (fPercent <= 0) :
        nTime = m_nTime
        nDelay = m_nDelay
        m_nTime = 0
        m_nDelay = 0
    else :
        nTime = round(float(m_nTime) * fPercent)
    nTime = nTime + nDelay
    CTmr = CTimer()
    CTmr.Set()
    while(True):
        if (CTmr.Get() >= nTime):
            break

    CTmr.Destroy()
# +일때는 시간, 아무것도 안넣으면(혹은 0) 동작시간, -일때는 동작시간에서 해당시간만큼 차감한 시간을 대기
def wait(nTime = 0):
    global m_nTime
    global m_nDelay
    if (not is_all_numbers(nTime)):
        if (nTime.find('%') > 0):
            wait_per(float(nTime.replace('%','')) / 100.0)
            return
    nDelay = 0
    if (nTime == 0) :
        nTime = m_nTime
        nDelay = m_nDelay
        m_nTime = 0
        m_nDelay = 0
    elif (nTime < 0) :
        nTime = m_nTime + nTime

    nTime = nTime + nDelay
    CTmr = CTimer()
    CTmr.Set()
    while(True):
        if (CTmr.Get() >= nTime):
            break

    CTmr.Destroy()
def TorqOn(*args):
    strRes = ""
    if (len(args) <= 0):
        strRes = "254:513:1"
    else:
        nIndex = 0
        for id in args:
            strRes = strRes + str(id) + ":513:1"
            if ((nIndex > 0) and (nIndex < len(args) - 1)):
                strRes = strRes + ","
            nIndex = nIndex + 1
    Send5(strRes)
def TorqOff(*args):
    strRes = ""
    if (len(args) <= 0):
        strRes = "254:513:1"
    else:
        nIndex = 0
        for id in args:
            strRes = strRes + str(id) + ":513:0"
            if ((nIndex > 0) and (nIndex < len(args) - 1)):
                strRes = strRes + ","
            nIndex = nIndex + 1
    Send5(strRes)
def Test():
    Connect()
    TorqOn(1)
    wait(1000)
    TorqOff(1)
    wait(1000)
    Disconnect()
def Test2():
    ################################################
    Connect()
    ################################################
    # TorqOn(1)
    Send(1000, 0, '1:-40,13:40,14:-20')
    wait()

    # TorqOff(1)
    Send(1000, 0, '1:-50,13,50,14,-30')
    wait()
    
    # TorqOn(1)
    Send(1000, 0, '1:0,13:0,14:0')
    wait()
    
    # TorqOff(1)
    ################################################
    Disconnect()
    ################################################
#Test()

url = "https://github.com/ojw5014/Released_DLL/blob/master/OpenJigWare.dll"
response = requests.get(url)

if response.status_code == 200:
    with open("OpenJigWare.dll_", "wb") as f:
        f.write(response.content)
    print("파일 다운로드 완료")
else:
    print("파일 다운로드 실패")