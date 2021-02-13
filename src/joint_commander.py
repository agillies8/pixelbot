#!/usr/bin/env python

#This note subscribes to the Image message and translates that into joint positions for the panels

import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from cv_bridge import CvBridge
import cv2

def image_callback(msg):

    #setup the publisher
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)

    #create bridge object for message translation
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(msg, "passthrough")

    #number of pixels in row and column. want to pull these over to pixelate at some point.
    col = 16
    row = 16

    #create joint state message and publish (note: this should use joint controller in the future, but using JS for now as POC)
    js = JointState()
    js.header = Header()
    js.header.stamp = rospy.Time.now()
    js.name = []

    #loop thru rows and cols to build JS message
    for i in range(1,row + 1):
        for j in range(1,col +1):
            js.name.append('{0}-{1}'.format(i,j)) #ideally this also get pulled out in the future
            js.position.append((255-img[i-1,j-1])*1.57/255) #set values, map from 8-bit greyscale to joint angle
    js.velocity = []
    js.effort = []
    pub.publish(js)


def commander():
    #create node and setup subscriber for image message
    rospy.init_node('commander')
    sub=rospy.Subscriber('image', Image, image_callback)

    while not rospy.is_shutdown():
        rospy.spin() #keep active

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass