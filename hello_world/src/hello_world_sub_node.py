#! /usr/bin/env python
import rospy
from std_msgs.msg import String # ROS Standard String Message Type

def onMessageReceived(data):
  rospy.loginfo("Received: %s" % (data.data))

def main():
    """
    ROS Node that subscribes to the greetings topic
    
    :return: None
    """
    # initialize ros node
    rospy.init_node('hello_world_sub')

    rospy.loginfo('Initiating Greeting Subscriber!')
    rospy.Subscriber('Greeting', String, onMessageReceived)

    # so the node doesn't exit
    rospy.spin()


if __name__ == '__main__':
    main()
