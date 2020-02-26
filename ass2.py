import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
GPIO.cleanup()

signvalues = []
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(36, GPIO.IN)

GPIO.setmode(GPIO.BOARD)
no=(GPIO.input(36)<<3)+(GPIO.input(16)<<2)+(GPIO.input(15)<<1)+GPIO.input(12)
	
print('Values:',no)

 





















	
	
	
	

