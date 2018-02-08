import serial

ser1 = serial.Serial('/dev/arduino-0', 115200, timeout=0.001)
ser2 = serial.Serial('/dev/arduino-1', 115200, timeout=0.001)
ser3 = serial.Serial('/dev/arduino-2', 115200, timeout=0.001)
ser4 = serial.Serial('/dev/arduino-3', 115200, timeout=0.001)

while True:
    response1 = ser1.readline()
    #print response1
    #print(response1[2:8])
    #print(response1[8:12])
    #print(response1[12:16])
    #print(response1[16:20])
    if len(response1)==23:
        if response1[0]=='#' and response1[20]=='$':
	    try:
		time1=int(response1[2:8], 16)
		yaw1=(int(response1[8:12], 16)-18000)/100.0
		roll1=(int(response1[12:16], 16)-18000)/100.0
		pitch1=(int(response1[16:20], 16)-18000)/100.0
		print '#1: ',time1,'\t',yaw1,'\t',roll1,'\t',pitch1
	    except:
		print("incorrent data.")

    response2 = ser2.readline()
    if len(response2)==23:
        if response2[0]=='#' and response2[20]=='$':
	    try:
		time2=int(response2[2:8], 16)
		yaw2=(int(response2[8:12], 16)-18000)/100.0
		roll2=(int(response2[12:16], 16)-18000)/100.0
		pitch2=(int(response2[16:20], 16)-18000)/100.0
                print '#2: ',time2,'\t',yaw2,'\t',roll2,'\t',pitch2
	    except:
		print("incorrent data.")

    response3 = ser3.readline()
    if len(response3)==23:
	if response3[0]=='#' and response3[20]=='$':
	    try:
		time3=int(response3[2:8], 16)
		yaw3=(int(response3[8:12], 16)-18000)/100.0
		roll3=(int(response3[12:16], 16)-18000)/100.0
		pitch3=(int(response3[16:20], 16)-18000)/100.0
		print '#3: ',time3,'\t',yaw3,'\t',roll3,'\t',pitch3
	    except:
		print("incorrent data.")

    response4 = ser4.readline()
    if len(response4)==23:
	if response4[0]=='#' and response4[20]=='$':
	    try:
		time4=int(response4[2:8], 16)
		yaw4=(int(response4[8:12], 16)-18000)/100.0
		roll4=(int(response4[12:16], 16)-18000)/100.0
		pitch4=(int(response4[16:20], 16)-18000)/100.0
		print '#4: ',time4,'\t',yaw4,'\t',roll4,'\t',pitch4
	    except:
		print("incorrent data.")

