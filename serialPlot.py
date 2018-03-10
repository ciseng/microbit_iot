import serial
import sys
from serial.tools.list_ports import comports as list_serial_ports
import matplotlib.pyplot as plt

plt.show()
ax = plt.axes(ylim=(0,255)) 
graph_line, = ax.plot([],[],'r-')

def guess_port():
    """
    From https://github.com/ntoll/microrepl
    Returns the port for the first micro:bit found connected to the computer
    running this script. If no micro:bit is found, returns None.
    """
    ports = list_serial_ports()
    platform = sys.platform
    if platform.startswith("linux"):
        for port in ports:
            if "VID:PID=0D28:0204" in port[2].upper():
                return port[0]
    elif platform.startswith("darwin"):
        for port in ports:
            if "VID:PID=0D28:0204" in port[2].upper():
                return port[0]
    elif platform.startswith("win"):
        for port in ports:
            if "VID:PID=0D28:0204" in port[2].upper():
                return port[0]
    return None

def main():
    try:
        port = guess_port()
        if port == None:
            print("No micro:bit detected!")
            sys.exit(1)

        ser = serial.Serial(port, baudrate=115200)
        count = 0
        xdata = []
        ydata = []
        
        print("Micro:bit connected and reading data from it.")
	while True:
	    serial_line = ser.readline()
            count = count + 1
            reading = int(serial_line)

            if(count < 100):
                ax.set_xlim(0,100)
            else:
                ax.set_xlim(count-50,count+50)
            xdata.append(count)
            ydata.append(reading)
            
            graph_line.set_xdata(xdata)
            graph_line.set_ydata(ydata)

            plt.draw()
            plt.pause(1e-17)

            if (count > 100):
               xdata.pop(0)
               ydata.pop(0)
            
    finally:
        ser.close()

main()
