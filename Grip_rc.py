import rospy
import numpy
from mavros_msgs.msg import OverrideRCIn

def gripper():
    rospy.init_node('Gripper', anonymous=True)
    pub = rospy.Publisher('/mavros/rc/override', OverrideRCIn, queue_size=1)
    RC = OverrideRCIn()
    low = True
    while not rospy.is_shutdown():
        low = not low
        if low:
            RC.channels[6] = 1500
            # RC.channels = numpy.array([0, 0, 0, 1500, 1325, 1560, 2000, 1500,1500,0,0,0,0,0,0,0,0,0], dtype=numpy.uint16)  
            print("done")      
            pub.publish(RC)
        else:
            RC.channels[6] = 0
            # RC.channels = numpy.array([0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0], dtype=numpy.uint16)  
            print("Low")      
            pub.publish(RC)
    
if __name__ == '__main__':
	try:
		gripper()
	except rospy.ROSInterruptException:
		pass