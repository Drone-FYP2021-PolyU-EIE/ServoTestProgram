#!/usr/bin/env python
import rospy
from mavros_msgs.msg import ActuatorControl

def gripper():
	rospy.init_node('Gripper', anonymous=True)

	pub = rospy.Publisher('/mavros/actuator_control', ActuatorControl, queue_size=10)

	rate = rospy.Rate(1)

	msg_out = ActuatorControl()
	msg_out.group_mix = 0
	msg_out.controls = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
	low = True

	while not rospy.is_shutdown():
		low = not low

		if low:
			msg_out.controls = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
			rospy.loginfo("Set servos low")
		else:
			msg_out.controls = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
			rospy.loginfo("Set servos high")

		msg_out.header.stamp = rospy.Time.now()
		pub.publish(msg_out)
		rate.sleep()

if __name__ == '__main__':
	try:
		gripper()
	except rospy.ROSInterruptException:
		pass