import time
import uuid
from multiprocessing import Process
from multiprocessing import Queue
import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])


def create_p(send_q, receive_q):
    p = Process(target=do, args=(send_q, receive_q,))
    p.start()


def do(send_q, receive_q):
    id = uuid.uuid1()
    print(id, "向send写入数据")
    info = {"id": id}
    send_q.put(info, block=True)
    while True:
        if receive_q.empty():
            print(id, "正在接受receive................")
            time.sleep(1)
            continue
        else:
            rec = receive_q.get()
            print(rec)
            break


send_q = Queue(maxsize=1)

receive_q = Queue(maxsize=1)
for i in range(1, 6):
    create_p(send_q, receive_q)
path = "./images/shot.png"
while True:
    c = 0
    if send_q.empty():
        time.sleep(1)
        continue
    result = reader.readtext(path)
    info = send_q.get()
    pid = info["id"]
    print(pid, "正在给处理中。。。。。")
    receive_q.put(str(pid) + ",ok")
