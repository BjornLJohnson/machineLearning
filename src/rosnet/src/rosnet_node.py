#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from nn_utils import *

# show_image(50, train_x_orig, train_y, classes)

# checkPerformance()


prediction_pub = rospy.Publisher('/nn_predictions', String, queue_size=10)

def image_cb(data):
    rospy.loginfo("That looks like a " + data.data + " to me" )
    #publish info to predictions topic

def classifier():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rosnet', anonymous=True)
    image_sub = rospy.Subscriber('/nn_classifier', Image, image_cb)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        classifier()
    except rospy.ROSInterruptException:
        pass
