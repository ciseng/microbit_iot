# microbit_iot
A simple light sensing application with micro:bit radio and serial.
Tested on a MAC. 

The description of this application is in my blog article [Micro:bit and the Internet of Things](https://cigdemsengul.blogspot.co.uk/).

For this application, we need two micro:bits and a laptop. Our application has three parts: 

* Sensing: One micro:bit will act as the sensing device, and will send its light measurements to a second micro:bit using its radio. 
* Communications gateway: The second micro:bit is the gateway and sends what it receives to the laptop over the serial. 
* Analytics and visualization: To show the incoming measurements the laptop runs a visualization scripts. 

## Making it work

Prerequisite: Python installed. 

1. Install _microbit-LightSensorSender.hex_ into the sensing micro:bit. 
2. Install _microbit-LightSensorReceiver.hex_ into the gateway micro:bit. 
3. Make sure you leave  the gateway micro:bit connected to your laptop (you would have needed to connect them to download the code into micro:bits). 
4. Download _serialPlot.py_ and run.  If the gateway micro:bit is not connected via serial, this script will give an error. Otherwise, it brings up a dynamic graph. 
5. Turn on the sensing micro:bit if you have not, and experiment with the set-up under different lighting conditions. 

An example of how things should look like is here: [Youtube video](https://youtu.be/_TmZ2PdWjbE)
