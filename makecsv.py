import serial
import datetime
import csv

com = serial.Serial("COM7", 9600) 
## first arduino-port, second baudrate

with open("test.csv", "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "acceleration", "co_x","co_y","co_z"])

while True:
    ## from Arduino date
    val = str(com.readline().decode("utf-8").rstrip("\n"))

    data = val.split(",")

    if len(data) == 4:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("test.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, data[0], data[1], data[2], data[3]])
