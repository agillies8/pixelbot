#!/usr/bin/env python

#This node grabs frames from the webcam, and publishes a pixelated version of the frame

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def pixelator():
    rospy.init_node('pixelator')
    pub=rospy.Publisher('image', Image, queue_size=1)
    rate=rospy.Rate(15)
    bridge = CvBridge() #create bridge object to translate cv image object to ros image message
    vid = cv2.VideoCapture(0)  #grab the webcam
    
    while not rospy.is_shutdown(): #do all this stuff in a loop

        ret, input = vid.read()  #grab a frame

        # Get input size
        height, width = input.shape[:2] 

        # Desired "pixelated" size
        w, h = (16, 16)

        #greyscale image
        gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

        #threshold for contrast: do white, inverse, do black, inverse back
        ret,thresh4 = cv2.threshold(gray,50,255,cv2.THRESH_TOZERO)
        thresh4_inv = cv2.bitwise_not(thresh4)
        ret,thresh5 = cv2.threshold(thresh4_inv,50,255,cv2.THRESH_TOZERO)
        thresh5_inv = cv2.bitwise_not(thresh5)

        # Resize input to "pixelated" size
        output = cv2.resize(thresh5_inv, (w, h), interpolation=cv2.INTER_LINEAR)

        #resize pixelated image back to original size for viewing as output image
        temp = cv2.resize(output, (width, height), interpolation=cv2.INTER_NEAREST)
        
        
        #show the images
        try:
            cv2.imshow('Input', input)
            cv2.imshow('Output', temp)
        except:
            pass

        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

        #translate and publish the message
        image_message = bridge.cv2_to_imgmsg(output, encoding="passthrough")
        pub.publish(image_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        pixelator()
    except rospy.ROSInterruptException:
        # After the loop release the video object 
        vid.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows() 
        pass