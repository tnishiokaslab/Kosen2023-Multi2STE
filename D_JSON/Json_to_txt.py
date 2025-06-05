import os
import json
import numpy as np

directory = "hdPose3d_stage1_coco19"
file_list = os.listdir(directory)
output_folder = 'output_files'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for file in file_list:
    with open(os.path.join('hdPose3d_stage1_coco19', file), 'r') as f:
        data = json.load(f)
        bodies = data['bodies']
        for body in bodies:
            id = body['id']
            joints19 = body['joints19']
            joints19 = [joints19[i] for i in range(len(joints19)) if i % 4 != 3]
            joints19 = np.array(joints19).reshape(-1,3)
            
            if os.path.exists(f'{output_folder}/output_{id}.txt'):
                joints19_befor = np.loadtxt(f'{output_folder}/output_{id}.txt')
                joints19_all = np.vstack((joints19_befor,joints19))
                np.savetxt(f'{output_folder}/output_{id}.txt', joints19_all)
            else:
                with open(f'{output_folder}/output_{id}.txt', "w") as file:
                    pass
                np.savetxt(f'{output_folder}/output_{id}.txt', joints19)

    