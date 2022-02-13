def get_apk():
    GITHUB_BASEURL = "https://github.com/openatx"
    __apk_version__ = '2.3.3'
    ret = []
    for name in ["app-uiautomator.apk", "app-uiautomator-test.apk"]:
        ret.append((name, "".join([
            GITHUB_BASEURL, "/android-uiautomator-server/releases/download/",
            __apk_version__, "/", name
        ])))
    print(ret)


def image():
    from PIL import Image
    import cv2
    import numpy as np
    image = Image.open("./images/xd1.png")
    nparr = np.array(image)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def image1():
    import cv2
    im = cv2.imread("./images/xd1.png", cv2.IMREAD_COLOR)


def str_test():
    source_path = "/home/why/work/python/pas/phone/1.png"
    path_split = source_path.split(".")
    path_dif = path_split[0]
    path_dif = path_dif + "dif"
    path_dif = path_dif + ".png"
    print(path_dif)


def time_test():
    import datetime
    import time
    before = datetime.datetime.now()
    time.sleep(4 * 60)
    after = datetime.datetime.now()
    print(after - before)


def dict_test():
    a = {"1": "one", "2": "tow", "3": "three"}
    for k in a:
        print(k)
        print(a[k])


dict_test()
