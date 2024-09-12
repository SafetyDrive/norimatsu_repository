import serial
import datetime
import csv

com = serial.Serial("COM7", 9600) 
## first arduino-port, second baudrate

with open("test.csv", "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ac_x","ac_y","ac_z"])

while True:
    ## from Arduino date
    val = str(com.readline().decode("utf-8").rstrip("\n"))

    data = val.split(",")

    if len(data) == 3:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("test.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, data[0], data[1], data[2]])
