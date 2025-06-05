import argparse
import time
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import sys
import re
from pathlib import Path

import torch
import torch.backends.cudnn as cudnn
from numpy import random
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
from yolov7.videomaker import videomaker
#from StridedTransformer.vis import get_pose2D,get_pose3D,img2video

from yolov7.utils.general import strip_optimizer
from yolov7.detect_or_track import detect
from yolov7.sort import *

parser = argparse.ArgumentParser()
parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
parser.add_argument('--gpu', type=str, default='', help='input video')
parser.add_argument('--source', type=str, default='inference\movies\shourin2.MOV', help='source')  # file/folder, 0 for webcam
parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--view-img', action='store_true', help='display results')
parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true', help='augmented inference')
parser.add_argument('--update', action='store_true', help='update all models')
parser.add_argument('--project', default='runs', help='save results to project/name')#######################
parser.add_argument('--name', default='detect_movie', help='save results to project/name')
parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
parser.add_argument('--no-trace', action='store_true', help='don`t trace model')

parser.add_argument('--track', action='store_true', help='run tracking')
parser.add_argument('--show-track', action='store_true', help='show tracked path')
parser.add_argument('--show-fps', action='store_true', help='show fps')
parser.add_argument('--thickness', type=int, default=2, help='bounding box and font size thickness')
parser.add_argument('--seed', type=int, default=1, help='random seed to control bbox colors')
parser.add_argument('--nobbox', action='store_true', help='don`t show bounding box')
parser.add_argument('--nolabel', action='store_true', help='don`t show label')
parser.add_argument('--unique-track-color', action='store_true', help='show each track in unique color')

parser.add_argument('--visualize', action='store_true', help='visualize features')
parser.add_argument('--data', type=str, default=ROOT / 'yolov7/data/coco128.yaml', help='(optional) dataset.yaml path')
parser.add_argument('--out-mask-style', default=False ,action='store_true', help='hide bbox')
parser.add_argument('--dnn', default=False ,action='store_true', help='hide bbox')



parser.add_argument('--alternate_crop_image', default=False ,action='store_true', help='alternate_crop_image')

opt = parser.parse_args()
opt.video = opt.source
print(opt)
np.random.seed(opt.seed)

sort_tracker = Sort(max_age=5,
                    min_hits=2,
                    iou_threshold=0.2) 

#check_requirements(exclude=('pycocotools', 'thop'))

with torch.no_grad():
    if opt.update:  # update all models (to fix SourceChangeWarning)
        
        for opt.weights in ['yolov7.pt']:
            detect(opt,sort_tracker)
            strip_optimizer(opt.weights)
        
    else:
        detect(opt,sort_tracker)

videomaker(video=opt.source ,pict_path= "runs/crop", output_dir="runs/cropvideo/")

