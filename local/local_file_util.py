from pathlib import Path


class LocalFileUtil:
    @staticmethod
    def read_as_list(path):
        lines = []
        p = Path(path)
        with p.open() as f:
            line = f.readline()
            while line:
                lines.append(line.replace("\n", ""))
                line = f.readline()
        return lines

    @staticmethod
    def read_as_dict(path):
        line_map = {}
        p = Path(path)
        with p.open() as f:
            line = f.readline()
            while line:
                lines = line.replace("\n", "")
                line = f.readline()


ls = LocalFileUtil.read_as_list("./devices")
print(ls)
