# Micropython on esp32

## 1. Install relevant packages
```python
pip install esptool
pip install adafruit_ampy
```

## 2. Download and install USB-to_UART driver
https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

## 3. Download Micropython firmware for ESP8266 boards
http://micropython.org/download#esp32

## 4. Deploy firmware
Using esptool.py erase the flash:
```python
esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
```

Deploy the new firmware:
```python
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin
```

## 5. REPL
Access REPL using:
```python
screen /dev/tty.SLAB_USBtoUART 115200
```

## 6. WiFi REPL
After a fresh install and boot the device configures itself as a WiFi access point (AP) that you can connect to. The ESSID is of the form MicroPython-xxxxxx. 

The password for the WiFi is micropythoN (note the upper-case N). 

Its IP address will be 192.168.4.1 once you connect to its network.
Connect using:
https://micropython.org/webrepl/

## 7. Upload, download, run scripts on the controller (AMPY)
### List
```python
ampy -p /dev/tty.SLAB_USBtoUART ls
```
### Download
```python
ampy -p /dev/tty.SLAB_USBtoUART get boot.py
```
if not working, try:
```python
ampy -p /dev/tty.SLAB_USBtoUART get boot.py > boot.py
```

### Upload
```python
ampy -p /dev/tty.SLAB_USBtoUART put boot.py
```

### Run
```python
ampy -p /dev/tty.SLAB_USBtoUART run main.py
```

## 8. Micropython documentation
https://docs.micropython.org/en/latest/index.html
