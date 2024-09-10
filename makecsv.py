import serial
import datetime
import csv

com = serial.Serial("COM7", 9600) 
## first arduino-port, second baudrate

with open("test.csv", "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Data1", "Data2"])

while True:
    ## from Arduino date
    val = str(com.readline().decode("utf-8").rstrip("\n"))

    data = val.split(",")

    if len(data) == 2:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("test.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, data[0], data[1]])