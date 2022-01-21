import cv2
import findit


def imread(filepath):
    return cv2.imread(filepath)


def match(target, detect):
    detect_img = imread(detect)
    target_img = imread(target)
    fi = findit.FindIt(engine=['template'],
                       engine_template_scale=(0.9, 1.1, 3),
                       pro_mode=True)
    fi.load_template("template", pic_object=detect_img)
    detect_img.shape[:2]
    raw_result = fi.find("target", target_pic_object=target_img)
    result = raw_result['data']['template']['TemplateEngine']
    target_sim = result['target_sim']
    x, y = result['target_point']
    return {"similarity": target_sim, "point": [x, y]}
