#!/usr/bin/env python
import rospy
from apriltag_ros.msg import AprilTagDetectionArray

class TagFilter:
    def __init__(self) -> None:
        rospy.init_node('apriltag_filter', anonymous=True)
        self.pub = rospy.Publisher('/tag_detections_filterred', AprilTagDetectionArray, queue_size=10)
        rospy.Subscriber("/tag_detections", AprilTagDetectionArray, self.callback)

        self.tag_array = AprilTagDetectionArray()
        self.rate = 10.0

    def callback(self, data):
        self.tag_array = data.detections.pose
        print(self.tag_array)

    def update(self):
        self.pub.publish(self.tag_array)
        
    def spin(self):
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.update()
            r.sleep()


if __name__ == '__main__':
    try:
        talker = TagFilter()
        talker.spin()
    except rospy.ROSInterruptException:
        pass