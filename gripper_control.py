
# Example of how to directly control a Pixhawk servo output with pymavlink.

import time
# Import mavutil
from pymavlink import mavutil

def set_servo_pwm(instance, microseconds):
    # master.set_servo(servo_n+8, microseconds) or:
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # first transmission of this command
        instance,  # servo instance, offset by 8 MAIN outputs
        microseconds, # PWM pulse-width
        0,0,0,0,0     # unused parameters
    )

# Create the connection
master = mavutil.mavlink_connection('/dev/ttyACM0',baud=57600)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# command servo_1 to go from min to max in steps of 50us, over 2 seconds
for us in range(1100, 1900, 50):
    set_servo_pwm(1, us)
    time.sleep(0.125)
