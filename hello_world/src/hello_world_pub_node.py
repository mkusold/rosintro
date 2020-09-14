#! /usr/bin/env python
import rospy
from std_msgs.msg import String # ROS Standard String Message Type

def main():
    """
    ROS Node that publishes hello world onto a topic
    
    :return: None
    """
    # initialize ros node
    rospy.init_node('hello_world_pub')

    rospy.loginfo('Initiating Greeting Publisher!')
    greetingPublisher = rospy.Publisher('Greeting', String, queue_size=10)

    while( not rospy.is_shutdown() ):
      greetingPublisher.publish("Hello World!")
      rospy.sleep(1)


if __name__ == '__main__':
    main()
