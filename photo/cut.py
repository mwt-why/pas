import cv2


def cut(filename, area, nf):
    """
        :param filename，裁剪的文件路径
        :param area，需要裁剪的区域((x1,y1),(x2,y2))
    """
    x1 = area[1][0]
    x2 = area[1][1]
    y1 = area[0][0]
    y2 = area[0][1]
    img = cv2.imread(filename)
    nimg = img[y1:y2, x1:x2]
    cv2.imwrite(nf, nimg)


def generate_filename(filename: str, fixed_suffix: str):
    """
    生成新的文件名，即在文件后面添加个s
    :param filename: 文件路径
    :param fixed_suffix: 新的文件后缀
    :return:
    """
    filename_info = filename.split(".")
    new_filename = filename_info[0] + fixed_suffix
    return new_filename + "." + filename_info[1]
