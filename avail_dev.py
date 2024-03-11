import serial
 
found = False
 
for i in range(64) :
  try :
    port = "/dev/ttyS%d" % i
    ser = serial.Serial(port)
    ser.close()
    print("Найден последовательный порт: ", port)
    found = True
  except serial.serialutil.SerialException :
    pass
 
if not found :
  print("Последовательных портов не обнаружено")
