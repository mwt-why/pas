from PIL import Image

base_image_path = '/home/why/workspace/python/pas/images'


def to_grey(d):
    img_path = base_image_path + '/' + d + '/screen.jpg'
    img = Image.open(img_path)
    img = img.convert('RGB')
    img = img.convert('L')
    img_path = base_image_path + '/' + d + '/0.jpg'
    img.save(img_path)
    return img


to_grey('0')
