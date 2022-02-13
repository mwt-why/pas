from word.my_ocr import MyOcr

path = "../images/shot.png"
my_ocr = MyOcr()
result = my_ocr.ocr(path)
for r in result:
    print(r)
