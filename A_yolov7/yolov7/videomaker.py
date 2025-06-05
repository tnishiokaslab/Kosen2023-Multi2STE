import sys
import argparse
import cv2
import os 
import numpy as np
import torch
import glob
from tqdm import tqdm
import copy
from IPython import embed
import re
sys.path.append(os.getcwd())
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
"""
pict_path="runs/crop"
video_path="input\movies\shourin2.MOV"
output_dir="runs/cropvideo/"
"""
os.environ["CUDA_VISIBLE_DEVICES"] = '0' #無理やりGPU使用



def videomaker(video, pict_path, output_dir):
    cap = cv2.VideoCapture(video)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    def atoi(text):#sortのkeyの何か
        return int(text) if text.isdigit() else text
    def natural_keys(text):
        return [ atoi(c) for c in re.split(r'(\d+)', text) ]

    dir = sorted(glob.glob(os.path.join(pict_path)+"\*"),key=natural_keys)

    for dir_path in dir:
        names = sorted(glob.glob(os.path.join(dir_path, '*.jpg')),key=natural_keys)
        name0 = str(names[0])
        img = cv2.imread(name0)
        size = (img.shape[1], img.shape[0])
        num = re.sub(r'\\', '/', dir_path).split('/')[-1]
        print(num)
        videoWrite = cv2.VideoWriter(output_dir + "cropvideo" + num +'.mp4', fourcc, fps, size) 

        for name_path in names:
            img = cv2.imread(name_path)
            videoWrite.write(img)
        videoWrite.release()