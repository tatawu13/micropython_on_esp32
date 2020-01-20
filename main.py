import time

while True:
    oled.fill(0)
    oled.text("Who's the man?", 10, 10)
    time.sleep(0.5)
    oled.show()
    
    oled.fill(0)
    oled.text("Who's the    ?", 10, 10)
    time.sleep(0.5)
    oled.show()