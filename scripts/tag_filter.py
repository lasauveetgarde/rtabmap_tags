#!/usr/bin/env python
import rospy
from apriltag_ros.msg import AprilTagDetectionArray
# from geometry_msgs import PoseWithCovarianceStamped

class TagFilter:
    def __init__(self) -> None:
        rospy.init_node('apriltag_filter', anonymous=True)
        self.pub = rospy.Publisher('/tag_detections_filterred', AprilTagDetectionArray, queue_size=10)
        rospy.Subscriber("/tag_detections", AprilTagDetectionArray, self.callback)

        self.tag_array = AprilTagDetectionArray()
        self.rate = 10

    def callback(self, data):
        # print(data.detections[0].pose)
        # print('\n\n====\n\n')
        new_arr = []
        for tag in data.detections:
            dst = (tag.pose.pose.pose.position.y**2 + tag.pose.pose.pose.position.z**2 + tag.pose.pose.pose.position.x**2)**0.5
            # print(dst)
            if dst < 1.5:
                print('\n\n  is here  \n\n')
                new_arr.append(tag)
        self.tag_array.detections = new_arr
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