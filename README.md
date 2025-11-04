# Esp32-WiFi-Scanner-using-MicroPython-and-OLED-display

A simple wifi scanner that is built with an ESP32 microcontroller, MicroPython, and a 0.96 SSD1306 OLED display.
This device scans for nearby wifi networks and shows the networks SSID,  signal strength (RSSI) and Authentication type 

Features 
- Scans for nearby WiFi networks
- Displays:
    - SSID
    - RSSI (Signal Strength)
    - Authentication Type (WPA2, Open, etc)
- Basic OLED interface
- BOOT button used to start the scan

Hardware Used 
- ESP32 Microcontroller
- SSD1306 OLED (0.96")
- 4 Jumper Wires
- Prototype Board

Wiring for the Display 
OLED Pin     ESP32 Pin 
VCC          3.3v 
GND          GND 
SDA          GPIO21
SCL          GPIO22

Setup 
1. Flash Micropython and the SSD1306 driver onto the ESP32
2. Use Thonny or mpremote to copy the files onto the ESP32
3. Save the code as main.py so it can run when ESP gets powered
4. Power on the ESP and test the scanning 
