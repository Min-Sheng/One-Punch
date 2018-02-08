import serial
import threading
import Queue

queue = Queue.Queue(1050)

def serial_read(ser):

    while True:
        package = ser.readline()
	if len(package)==23:
            if package[0]=='#' and package[20]=='$':
	        try:
                    number=package[0:2]
		    time=int(package[2:8], 16)
		    yaw=(int(package[8:12], 16)-18000)/100.0
		    roll=(int(package[12:16], 16)-18000)/100.0
		    pitch=(int(package[16:20], 16)-18000)/100.0
		    data = number+':\t'+str(time)+'\t'+str(yaw)+'\t'+str(roll)+'\t'+str(pitch)
		    queue.put(data)
	        except:
                    continue

ser1 = serial.Serial('/dev/arduino-0', 115200, timeout=0.001)
ser2 = serial.Serial('/dev/arduino-1', 115200, timeout=0.001)
ser3 = serial.Serial('/dev/arduino-2', 115200, timeout=0.001)
ser4 = serial.Serial('/dev/arduino-3', 115200, timeout=0.001) 

thread1 = threading.Thread(target=serial_read, args=(ser1,),).start()
thread2 = threading.Thread(target=serial_read, args=(ser2,),).start()
thread3 = threading.Thread(target=serial_read, args=(ser3,),).start()
thread4 = threading.Thread(target=serial_read, args=(ser4,),).start()

#count=0
refresh=[0,0,0,0]
while True:

    data = queue.get()
    number = data[1]
    if number=='1':
        data1 = data
	refresh[0]=1
    elif number=='2':
        data2 = data
	refresh[1]=1
    elif number=='3':
        data3 = data
	refresh[2]=1
    elif number=='4':
        data4 = data
	refresh[3]=1
    if refresh[0]==1 and refresh[1]==1 and refresh[2]==1 and refresh[3]==1:
        print data1,'\n',data2,'\n',data3,'\n',data4
        #print count
        #count=count+1
	refresh=[0,0,0,0]

