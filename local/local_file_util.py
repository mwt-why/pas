from pathlib import Path


def read_as_list(path):
    lines = []
    p = Path(path)
    with p.open() as f:
        line = f.readline()
        while line:
            lines.append(line.replace("\n", ""))
            line = f.readline()
    return lines


def read_as_nlist(path):
    result = []
    p = Path(path)
    with p.open() as f:
        line = f.readline()
        while line:
            line = line.replace("\n", "")
            k_v = line.split(":")
            result.append(k_v)
            line = f.readline()
    return result


def get_account():
    path = "./config/user_queue"
    acc_list = read_as_nlist(path)
    if len(acc_list) == 0:
        return None
    account = acc_list.pop()
    with open(path, "w") as w:
        for acc in acc_list:
            w.write(acc[0] + ":" + acc[1])
    return account



