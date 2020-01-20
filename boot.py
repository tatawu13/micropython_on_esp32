import esp, gc
esp.osdebug(None)

import machine, ssd1306, util

oled = util.start_oled()
oled.text("...", 1,1)
oled.show()

gc.collect()
