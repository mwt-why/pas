import uiautomator2 as u2

image_dir = '../images/'


def shot_image(serial):
    d = u2.connect(serial)
    d.shell("screencap /sdcard/screen.png")
    d.pull("/sdcard/screen.png", image_dir + serial + ".png")


def input_word():
    d = u2.connect("936X1XHD9")
    d.set_clipboard("hello world")
    d.clipboard
    d.click(1048, 488)


# shot_image("emulator-5554")
# d = u2.connect("emulator-5554")
# d.app_start("com.netease.pm02")
d1 = u2.connect_wifi("192.168.31.92")
# d1 = u2.connect_adb_wifi("192.168.42.236:5555")
# d1 = u2.connect("192.168.31.7")
print(d1.info)
