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
from pathlib import Path

sys.path.append(os.getcwd())
from model.strided_transformer import Model
from common.camera import *

import matplotlib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

import time
start_timer = time.time() #時間計測開始

# memory management
matplotlib.interactive(False)

plt.switch_backend('agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

txt =  'runs\santa\pose3dtxt\santapose3d.txt'
out_txt = np.loadtxt(txt)
out_txt_1 = out_txt.reshape(len(out_txt)//17, 17, 3)


def show3Dpose(vals, ax):
    ax.view_init(elev=15., azim=70)

    I = np.array( [0, 0, 1, 4, 2, 5, 0, 7,  8,  8, 14, 15, 11, 12, 8,  9])
    J = np.array( [1, 4, 2, 5, 3, 6, 7, 8, 14, 11, 15, 16, 12, 13, 9, 10])

    LR = np.array([0, 1, 0, 1, 0, 1, 0, 0, 0,   1,  0,  0,  1,  1, 0, 0], dtype=bool)

    for i in np.arange( len(I) ):
        x, y, z = [np.array( [vals[I[i], j], vals[J[i], j]] ) for j in range(3)]

        ax.plot(x, y, z, lw=2)
        ax.scatter(x, y, z)

    RADIUS = 0.8

    ax.set_xlim3d([-RADIUS, RADIUS])
    ax.set_ylim3d([-RADIUS, RADIUS])
    #ax.set_aspect('equal') # works fine in matplotlib==2.2.2
    ax.set_aspect('auto')

    white = (1.0, 1.0, 1.0, 0.0)
    ax.xaxis.set_pane_color(white) 
    ax.yaxis.set_pane_color(white)
    ax.zaxis.set_pane_color(white)

    ax.tick_params('x', labelbottom = False)
    ax.tick_params('y', labelleft = False)
    ax.tick_params('z', labelleft = False)





for i in tqdm(range(len(out_txt)//17)):
    post_out = out_txt_1[i,:,:].astype(np.float32)
    
    rot =  [0.1407056450843811, -0.1500701755285263, -0.755240797996521, 0.6223280429840088]
    rot = np.array(rot, dtype='float32')
    post_out = camera_to_world(post_out, R=rot, t=0)
    post_out[:, 2] -= np.min(post_out[:, 2])


    fig = plt.figure( figsize=(9.6, 5.4))
    gs = gridspec.GridSpec(1, 1)
    gs.update(wspace=-0.00, hspace=0.05) 
    ax = plt.subplot(gs[0], projection='3d')
    
    show3Dpose( post_out, ax)
    
    output_dir_3D = 'pose3D/'
    os.makedirs(output_dir_3D, exist_ok=True)
    plt.savefig(output_dir_3D + str(('%04d'% i)) + '_3D.png', dpi=200, format='png', bbox_inches = 'tight')



