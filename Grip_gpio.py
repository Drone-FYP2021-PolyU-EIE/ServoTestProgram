import Jetson.GPIO as GPIO
import time

# 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

output_pins = 33
output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception("No PWM")

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output_pin, GPIO.OUT, initial = GPIO.HIGH)
    p = GPIO.PWM(output_pin, 50)
    p.start(25)

    print("PWM running")
    try:
        while True:
            time.sleep(1)
    finally:
        p.stop()
        GPOI.cleanup()

if __name__ == '__main__':
    main()
