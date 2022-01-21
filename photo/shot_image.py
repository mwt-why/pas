import uiautomator2 as u2

image_dir = '/home/tommy/shot/'


def shot_image(d):
    d.shell("screencap /sdcard/screen.png")
    d.pull("/sdcard/screen.png", image_dir + "shot" + ".png")


if __name__ == '__main__':
    d1 = u2.connect()
    # d1 = u2.connect_wifi("192.168.31.7")
    shot_image(d1)
