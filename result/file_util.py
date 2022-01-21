def write_line(filepath, content):
    with open(filepath, "a") as w:
        w.write(content + "\n")

