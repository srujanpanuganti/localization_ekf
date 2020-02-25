#!/usr/bin/env python

#importing rospy to use ROS with python client 
import rospy
import numpy as np

#We will subscribe to this laserscan data to to identfy obstacles 
from sensor_msgs.msg import LaserScan

# We import the Twist topic from the geometry_msgs to publish our messages to the turtlebot
from geometry_msgs.msg import Twist

