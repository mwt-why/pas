import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from object_detection.utils import visualization_utils as viz_utils
from six import BytesIO
from object_detection.utils import label_map_util
from object_detection.utils import config_util
from object_detection.builders import model_builder
import matplotlib
matplotlib.use('tkagg')

path2config = '/home/why/dataset/result/pipeline.config'
path2model = '/home/why/dataset/result/saved_model/saved_model.pb'
path2checkpoint = '/home/why/dataset/result/checkpoint'

configs = config_util.get_configs_from_pipeline_file(path2config)
model_config = configs['model']
detection_model = model_builder.build(
    model_config=model_config, is_training=False)

ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(path2checkpoint, 'ckpt-0')).expect_partial()

path2lable_map = '/home/why/dataset/train/game_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(
    path2lable_map, use_display_name=True)


def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections, prediction_dict, tf.reshape(shapes, [-1])


def load_image_into_numpy_array(path):
    img_data = tf.io.gfile.GFile(path, 'rb').read()
    image = Image.open(BytesIO(img_data))
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


image_path = '/home/why/workspace/python/pas/images/0/screen.jpg'


def get_detected_result():
    image_np = load_image_into_numpy_array(image_path)
    input_tensor = tf.convert_to_tensor(
        np.expand_dims(image_np, 0), dtype=tf.float32)
    detections, predictions_dict, shapes = detect_fn(input_tensor)

    boxes = detections['detection_boxes'].numpy()[0]
    # get all boxes from an array
    max_boxes_to_draw = boxes.shape[0]
    # get scores to get a threshold
    scores = detections['detection_scores'].numpy()[0]
    # this is set as a default but feel free to adjust it to your needs
    min_score_thresh = .5
    # # iterate over all objects found
    coordinates = []
    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores[i] > min_score_thresh:
            class_id = int(detections['detection_classes'].numpy()[0][i] + 1)
            coordinates.append({
                "box": boxes[i],
                "class_name": category_index[class_id]["name"],
                "score": scores[i]
            })
    return coordinates

coordinates = get_detected_result()
print(coordinates)
