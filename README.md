# pixelbot
The Pixelbot robot art piece

This uses the webcam to create a simualted image on an array of mechanically actuated panels.

Current status (2-14-2021): All working in code, but need to build it. More details on physical design to follow...

To start:
1) You must install ROS melodic on an Ubuntu system
2) Attach webcam to your system
3) Clone this repo into the /src dir of your catkin workspace and make it
4) Start with this command: roslaunch pixelbot display.launch

Key resources
-Inspired by this work: https://www.youtube.com/watch?v=kV8v2GKC8WA&t=394s&ab_channel=WIRED
-Creating a URDF from solidworks: http://wiki.ros.org/sw_urdf_exporter (I just used this as a starting point, then created a small script to make the rest since doing it all by hand would be nuts)
-How to go between ROS Image messages and OpenCV image formats: http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython
-Basic primer on thresholding in OpenCV: https://docs.opencv.org/3.4/db/d8e/tutorial_threshold.html
-Useful note on pixelating an image using OpenCV: https://stackoverflow.com/questions/47143332/how-to-pixelate-a-square-image-to-256-big-pixels-with-python/51547855#51547855

