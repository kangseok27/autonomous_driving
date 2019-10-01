#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import PoseStamped


#topic subscriber
def callback(msg):
	print msg.pose


#goal_pose
def pose_stamped(self):
	pose = PoseStamped()
	pose.header.stamp = rospy.Time.now()
	pose.header.frame_id = "map"
	pose.pose.position.x = self[0][0]
	pose.pose.position.y = self[0][1]
	pose.pose.position.z = self[0][2]

	#quaternion = tf.transformations.quaternion_from_euler(0, 0, self.theta)
	pose.pose.orientation.x = self[1][0]
	pose.pose.orientation.y = self[1][1]
	pose.pose.orientation.z = self[1][2]
	pose.pose.orientation.w = self[1][3]

	return pose


#main_node
if __name__ == '__main__':
	rospy.init_node('main_node')

	pub_ps=rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
	sub_int=rospy.Subscriber('/move_base_simple/goal', PoseStamped, callback)

	rate=rospy.Rate(2)

	pose_val=[(2.1, 2.2, 0.0), (0.0, 0.0, 0.0, 1.0)]

	print('start!')

	while not rospy.is_shutdown():

		pose=pose_stamped(pose_val)
		pub_ps.publish(pose)

		rate.sleep()



