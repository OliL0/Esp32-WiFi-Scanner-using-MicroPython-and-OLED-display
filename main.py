from machine import Pin, I2C
import ssd1306
import network
import time

#establishes the communication with the ssd1306 screen
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

button_scan = Pin(0, Pin.IN, Pin.PULL_UP)#pin.IN is an input and pull up reepresents the behaviour of when it is pressed 

wlan = network.WLAN(network.STA_IF)#sets up the environment for wlan
wlan.active(True)
time.sleep(0.5)

oled.fill(0)
oled.text("ESP WiFi Scanner", 0, 0)
oled.text("Booting up...", 0, 16)
oled.show()
time.sleep(1)

oled.fill(0)
oled.text("Press BOOT to scan networks", 0, 0)
oled.show()

def scan_and_show():
    auth_modes = {
            0: "Open",
            1: "WEP",
            2: "WPA-PSK",
            3: "WPA2-PSK",
            4: "WPA/WPA2-PSK",
            5: "WPA2-ENT",
    }
    wifi = wlan.scan()
    oled.fill(0)
    oled.text("Networks: " + str(len(wifi)), 0, 0)
    y = 10
    
    for net in wifi: #loop for scanning results 
        ssid = net[0].decode ('utf-8', 'replace')#net[0] = wifi name and the .decode part converts bytes into readable and avoids crashes with replace
        rssi = net[3]# signal strength that is recieved
        auth_type = auth_modes.get(net[4], "?")
        oled.text(ssid, 0, y)#draws the ssid on the line above the rssi and auth
        line2 = "{} dB {}".format(rssi, auth_type)#draws RSSI + auth on the line under ssid 
        oled.text(line2, 0, y + 10)
        y += 20 #increments to leave space 
        
    oled.show()#makes it so the text is visable 

while True:
    if button_scan.value() == 0:
        oled.fill(0)
        oled.text("Scanning...", 0, 0)
        oled.show()
        scan_and_show()
