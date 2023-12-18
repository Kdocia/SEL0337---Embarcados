import cv2
import os
import time
from picamera2 import Picamera2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definição do pino do botão:
GPIO.setup(15, GPIO.IN, GPIO.PUD_UP)

# Definição do pino do led
GPIO.setup(23, GPIO.OUT)

face_detector = cv2.CascadeClassifier(
    "/home/sel/Desktop/pratica6/haarcascade_frontalface_default.xml")

cv2.startWindowThread()

picam2 = Picamera2()

picam2.configure(picam2.create_preview_configuration(
    main={"format": 'XRGB8888', "size": (640, 480)}))

picam2.start()

output_directory = "detected_faces"

os.makedirs(output_directory, exist_ok=True)
try:
    while True:
        if not GPIO.input(15):
            GPIO.output(23, GPIO.HIGH)
            im = picam2.capture_array()

            grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(grey, 1.1, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0))

                timestamp = int(time.time())
                filename = os.path.join(
                    output_directory, f"face_{timestamp}.jpg")

                cv2.imwrite(filename, im[y:y+h, x:x+w])

            cv2.imshow("Camera", im)
            GPIO.output(23, GPIO.LOW)

            cv2.waitKey(1)

except KeyboardInterrupt:
    GPIO.cleanup()  # toda vez que interrompermos o programa com crtl C o pino vai ser limpado automaticmanete
