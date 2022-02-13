import uiautomator2 as u2

image_dir = '../images/'


def shot_image(d):
    d.shell("screencap /sdcard/screen.png")
    d.pull("/sdcard/screen.png", image_dir + "shot" + ".png")


if __name__ == '__main__':
    import cv2

    d1 = u2.connect()
    # d1 = u2.connect_wifi("192.168.31.7")
    # shot_image(d1)
    d1.screenshot()
    image = d1.screenshot(format='opencv')
    cv2.imwrite(image_dir + "shot" + ".png", image)
