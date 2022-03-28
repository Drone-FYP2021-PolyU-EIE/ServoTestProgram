from sunau import AUDIO_FILE_ENCODING_LINEAR_16
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
# ang = 180
# kit.servo[0].angle = ang

for i in range(0,180):
    kit.servo[0].angle = i
    time.sleep(0.05)