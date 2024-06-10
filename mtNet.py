from mmdet.apis import init_detector, inference_detector
from mmdet.registry import VISUALIZERS
import mmcv

config_file = 'configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py'

# 從 model zoo 下載 checkpoint 並放在 `checkpoints/` 文件下
# 網址為: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco.pth'
device = 'cuda:0'
# 初始化檢測器
model = init_detector(config_file, checkpoint_file, device=device)
# 推理演示圖像
img = 'demo/demo.jpg'
result = inference_detector(model, img)
print(result)

# from mmdet.apis import init_detector, inference_detector
# from mmdet.registry import VISUALIZERS
# import cv2
# import mmcv

# config_file = 'configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py'
# checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco.pth'
# device = 'cuda:0'
# model = init_detector(config_file, checkpoint_file, device=device)

# visualizer = VISUALIZERS.build(model.cfg.visualizer)

# visualizer.dataset_meta = model.dataset_meta

# img = 'demo/demo.jpg'
# img = cv2.imread(img)

# result = inference_detector(model, img)

# img = mmcv.imconvert(img, 'bgr', 'rgb')
# visualizer.add_datasample(
# name='result',
# image=img,
# data_sample=result,
# draw_gt=False,
# pred_score_thr=0.3,
# show=False)

# img = visualizer.get_image()
# img = mmcv.imconvert(img, 'bgr', 'rgb')
# cv2.imshow('result', img)

# cv2.waitKey(0)