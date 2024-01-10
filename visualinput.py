import cv2
import numpy as np
import sys

class Visualinput:
    def __init__(self, window_name='Webcam Viewer'):
        self.window_name = window_name
        self.capture = cv2.VideoCapture(0)
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([80, 255, 255])
        self.found_contour = False

        self.cy = sys.maxsize
        self.cx = sys.maxsize

        self.show_image()

    def __del__(self):
        self.capture.release()
        cv2.destroyAllWindows()

    def decideJump(self):
        if self.cy < 150:
            return True
        else:
            return False

    def get_center(self):
        print(self.cy)
        return self.cx, self.cy

    def process_image(self, frame):
        #convert image to HSV-format
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #blur image to get cleaner contours
        #blur = cv2.GaussianBlur(hsv, (5, 5), 0)
        #mask image
        mask = cv2.inRange(hsv, self.lower_green, self.upper_green)
        #find contours in masked image
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #make result image
        result = cv2.bitwise_and(frame, frame, mask= mask)

        return result, contours

    def show_image(self):
        #get frame from webcam
        ret, frame = self.capture.read()

        result, contours = self.process_image(frame)
    
        if contours:
            biggest_contour = max(contours, key=cv2.contourArea)

            M = cv2.moments(biggest_contour)
            if M["m00"] != 0 and cv2.contourArea(biggest_contour) > 400:
                self.found_contour = True

                self.cx = int(M["m10"] / M["m00"])
                self.cy = int(M["m01"] / M["m00"])

                cv2.circle(frame, (self.cx, self.cy), 10, (0, 0, 255), -1)
            else:
                self.found_contour = False

        cv2.imshow(self.window_name, frame)
        """
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break"""

if __name__ == "__main__":
    webcam_viewer = Visualinput()
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        webcam_viewer.show_image()
