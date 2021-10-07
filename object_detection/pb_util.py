from comm_const import CommConst
import tensorflow as tf
from google.protobuf import text_format
import item_pb2

def load_pbtxt_file(path):
    if not tf.io.gfile.exists(path):
        raise ValueError('`path` is not exist.')

    with tf.io.gfile.GFile(path, 'r') as fid:
        pbtxt_string = fid.read()
        pbtxt = item_pb2.ItemInfo()
        text_format.Merge(pbtxt_string, pbtxt)
    return pbtxt


def get_pbtxt_id(name):
    item_info = load_pbtxt_file(CommConst.label_map_path)
    for item in item_info.item:
        if item.name == name:
            return item.id
    return 0


