import glob
import os

image_files = glob.glob("/Users/pakistanleong/workspace/opencv/darknet/training_data/images/*.jpg")

fo = open("/Users/pakistanleong/workspace/opencv/darknet/model/train.txt", "w")


for image_file in image_files:
    fo.write(image_file)
    fo.write(os.linesep)
