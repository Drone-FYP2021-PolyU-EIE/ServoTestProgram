import time
import rospy
# from adafruit_servokit import ServoKit
from ros_circuitpython_servokit_msgs.msg import AllServoAngle

def gripper():
    rospy.init_node('Gripper', anonymous=True)
    servo_pub = rospy.Publisher('/servo/angle', AllServoAngle, queue_size=10)
    angle = AllServoAngle()
    angle.all16servoPWM = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while not rospy.is_shutdown():
        for i in range(0,180):
            angle.all16servoPWM[0] = i
            servo_pub.publish(angle)
            time.sleep(0.05)

if __name__ == '__main__':
	try:
		gripper()
	except rospy.ROSInterruptException:
		pass