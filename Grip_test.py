import rospy
from geometry_msgs.msg import Twist

def gripper():
    rospy.init_node('Gripper', anonymous=True)
    pub =  rospy.Publisher('/mavros/setpoint_velocity', Twist , queue_size=10)
    rate = rospy.Rate(10)

    msg  = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    while not rospy.is_shutdown():
        rospy.loginfo("Set servos")
        msg.linear.x = 10
        msg.linear.y = 10
        msg.linear.z = 10
        msg.angular.x = 1
        msg.angular.y = 1
        msg.angular.z = 1
        pub.publish(msg)
        rate.sleep()
    
if __name__ == '__main__':
	try:
		gripper()
	except rospy.ROSInterruptException:
		pass
    