
# Example of how to directly control a Pixhawk servo output with pymavlink.

import time
# Import mavutil
from pymavlink import mavutil

def set_servo_pwm(servo_n, microseconds):
    # master.set_servo(servo_n+8, microseconds)
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # first transmission of this command
        servo_n,  # servo instance, offset by 8 MAIN outputs
        microseconds, # PWM pulse-width
        0,0,0,0,0     # unused parameters
    )

# Create the connection
# master = mavutil.mavlink_connection('/dev/ttyUSB0')
master = mavutil.mavlink_connection('/dev/ttyACM0',baud=57600)
# master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
print("ok")
# master = mavutil.mavlink_connection('udp:0.0.0.0:{}'.format(1))
# Wait a heartbeat before sending commands
master.wait_heartbeat()
print("wait")

# command servo_1 to go from min to max in steps of 50us, over 2 seconds
for us in range(1100, 2000, 10):
    print("start")
    set_servo_pwm(1, us)
    time.sleep(0.1)
