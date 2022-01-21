import uiautomator2 as u2
import time

d = u2.connect_wifi("192.168.31.7")
d.set_clipboard("32454324")
d.clipboard
d.click(1080, 393)
time.sleep(1)
d.long_click(1080, 393, 2)
