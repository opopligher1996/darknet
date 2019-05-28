


Label the data
1. cd labelImg/
2. python3 labelImg.py
3. choose 'yolo' format
4. choose the Save Dir


Detect
./darknet detect /Users/pakistanleong/workspace/opencv/darknet/model/yolov3-tiny-test.cfg /Users/pakistanleong/workspace/opencv/darknet/model/weights/yolov3-tiny_8 0.weights /Users/pakistanleong/workspace/opencv/darknet/training_data/images/20190518_102551_minibus_12_2.jpg -thresh 0.01

./darknet detect /content/workspace/darknet/model/yolov3-tiny-test.cfg  /content/workspace/darknet/model/weights/yolov3-tiny_1000.weights  /content/workspace/darknet/training_data/images/20190518_102551_minibus_12_2.jpg -thresh 0.01

Train Model
./darknet detector train /Users/pakistanleong/workspace/opencv/darknet/model/obj.data /Users/pakistanleong/workspace/opencv/darknet/model/yolov3-tiny.cfg /Users/pakistanleong/workspace/opencv/darknet/model/weights/yolov3-tiny_60.weights

Retrain Model
./darknet detector train cfg/obj.data cfg/yolo-obj.cfg yolo-obj_2000.weights

Test Model
./darknet detector test /Users/pakistanleong/workspace/opencv/darknet/model/obj.data /Users/pakistanleong/workspace/opencv/darknet/model/yolov3-tiny-test.cfg /Users/pakistanleong/workspace/opencv/darknet/model/weights/yolov3-tiny_60.weights /Users/pakistanleong/workspace/opencv/darknet/training_data/images/20190518_102551_minibus_12_2.jpg -thresh 0.01


./darknet detector test /Users/pakistanleong/workspace/opencv/darknet/model/obj.data /Users/pakistanleong/workspace/opencv/darknet/model/yolov3-tiny.cfg /Users/pakistanleong/workspace/opencv/darknet/model/weights/yolov3-tiny_60.weights /Users/pakistanleong/workspace/opencv/darknet/training_data/images/20190518_102551_minibus_12_2.jpg

./darknet detector test /content/workspace/darknet/model/obj.data /content/workspace/darknet/model/yolov3-tiny-test.cfg /content/workspace/darknet/model/weights/yolov3-tiny_1000.weights /content/workspace/darknet/training_data/images/20190518_102551_minibus_12_2.jpg

Cal Anchors
In /Users/pakistanleong/Desktop/darknet/
./darknet detector calc_anchors /Users/pakistanleong/workspace/opencv/darknet/model/obj.data -num_of_clusters 6 -width 416 -height 416
