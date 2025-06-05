main:
	cd A_yolov7 && python main.py  --no-trace --track --classes 0 --source inference\movies\clopped_hagging_a1_09.mp4
	cd B_StridedTransformer-Pose3D && python demo/vis.py --video sample_video.mp4
	cd B_StridedTransformer-Pose3D && python txt_to_3dpose.py
	cd C_plot3d_with_html && python plot3d.py
	