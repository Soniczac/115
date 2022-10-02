import cv2
import os 

path = "Images/"
images = ["111.jpg", "112.jpg", "113.jpg", "114.jpg" , "115.jpg", "116.jpg", "117.jpg", "1148.jpg", "119.jpg", "120.jpg"]
os.listdir(path)

if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name = path+"/"+file

   size = (width, height)

out = cv2.VideoWriter('project.avi' ,cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)