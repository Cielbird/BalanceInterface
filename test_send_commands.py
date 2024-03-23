import serial

port = '/dev/cu.usbmodem1301'  # remplacer avec le port série nécessaire
baud_rate = 115200 
ser = serial.Serial(port, baud_rate)


def sendTareCommand(arduino):
    """
    envoie 't' à l'arduino: la commande de tare
    """
    command = "t"      
    arduino.write(bytearray(str(command), 'utf-8'))

def sendCalibCommand(arduino, A, B):
    """
    envoie 'c [Constante A] [Constante B]' à l'arduino: la commande d'étalonnage et ses constantes
    """
    command = f"c {A} {B}"
    arduino.write(bytearray(str(command), 'utf-8'))

try:
    commandIn = input("Enter command (1 or 2): ")
    if(commandIn == '1'):
        sendTareCommand(ser)
    elif(commandIn == '2'):
        A = float(input("Enter constant A: "))
        B = float(input("Enter constant B: "))
        sendCalibCommand(ser, A, B)
except serial.SerialException as var:
    print(var)
finally:
    ser.close()
