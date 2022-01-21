from word.my_ocr import MyOcr

path = "/home/tommy/shot/shot.png"
my_ocr = MyOcr()
result = my_ocr.ocr(path)
for r in result:
    print(r)
