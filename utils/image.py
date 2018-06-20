import cv2
import os

def video2images(video_file='',saved_path='',prefix='',every_frames=1,max_frames=0):
    frame_count = 0
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    video_capture = cv2.VideoCapture(fn)
    success, frame = video_capture.read()
    if not success:
        print('Failed to open video,please check your video')
    while success:
        frame_count += 1
        if frame_count%every_frames == 0:
            saved_name = os.path.join(saved_path,'%s_%s_%d.jpg'%(prefix,os.path.basename(video_file).split()[0],frame_count))
            cv2.imwrite(saved_name,frame)
        if max_frames>0 and frame_count == max_frames:
            break
        success, frame = video_capture.read()
    video_capture.release()
