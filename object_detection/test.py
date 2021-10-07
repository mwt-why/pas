import json
from comm_const import CommConst
with open(CommConst.label_map_path,'r') as load_f:
    load_json = json.load(load_f)
    print(load_json)
