def sendToArduino(sendStr, ser):
    ser.write(sendStr.encode())

# ======================================


def recvFromArduino(ser):
    startMarker = 60
    endMarker = 62

    ck = ""
    x = "z"  # any value that is not an end- or startMarker
    byteCount = -1  # to allow for the fact that the last increment will be one too many

    # wait for the start character
    while ord(x) != startMarker:
        x = ser.read()

    # save data until the end marker is found
    while ord(x) != endMarker:
        if ord(x) != startMarker:
            ck = ck + str(x)
            byteCount += 1
        x = str(ser.read(), 'utf-8')

    return(ck)

# ============================


def waitForArduino(ser):

   # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
   # it also ensures that any bytes left over from a previous message are discarded

    startMarker = 60
    endMarker = 62

    msg = ""
    while msg.find("Arduino is ready") == -1:

        while ser.inWaiting() == 0:
            pass

        msg = recvFromArduino(ser)

        print(msg)

# ======================================


def sendAlarmSignal(sig, ser):
    waitingForReply = False
    n = 0
    sendstr = buildSigMsg(sig)

    if waitingForReply == False:
        sendToArduino(sendstr, ser)
        waitingForReply = True

    if waitingForReply == True:

        while ser.inWaiting() == 0:
            pass

        dataRecvd = recvFromArduino(ser)
        # print("REC:  " + dataRecvd)
        waitingForReply = False

        # print("===========")


# ======================================

def buildSigMsg(sig):
    startMarker = "<"
    endMarker = ">"
    return startMarker + str(sig) + endMarker
