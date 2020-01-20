import ssd1306, machine, time

def start_oled(scl_pin=15, sda_pin=4, reset_pin=16, w=128, h=64):
    
    p_rst = machine.Pin(reset_pin, machine.Pin.OUT)
    p_rst.value(0)
    time.sleep(0.1)
    p_rst.value(1)

    i2c = machine.I2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
    oled = ssd1306.SSD1306_I2C(w, h, i2c)
    oled.fill(0)
    return oled 
