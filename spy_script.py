##################################################################
#             Library Imports and Global Variables
##################################################################

import cv2         # Library concepted to solve Video Tracking tasks. 
import threading   # Library that allows us run multiple tasks simultaneously.
import playsound   # Library that allows to the script to play sounds.

spy_lock = threading.Lock()
spy_fire = cv2.CascadeClassifier('spy_models.xml') # Loads the XML models file.
spy_video = cv2.VideoCapture(0) # Use 0 for integrated WebCam. // 1 for USB WebCam.
spy_message = """
######## Spy's Fire Detector™ ########
    
Welcome to my project. This was initally a Hackathon Project, and after
the competition ended(and earned a cash prize, yey! :]] ), I decided to
publish this to my GitHub Page as a reference for better projects than 
this.

Have fun! If you have any issues/optimisation ideas, contact me via
https://okspy.codes // GitHub.
    
######## Spy's Fire Detector™ ########
"""
print(spy_message)


##################################################################
#                             Runtime
##################################################################	
def spy_play_alarm():
    playsound.playsound('spy_alarm.mp3',True) # Loads the alarm sound that will be played when the fire is detected.
    print("github@okspy.codes: Fire has dissapeared.")
    print("######## Spy's Fire Detector™ ########")
    spy_lock.release()
	
while(True):
    Alarm_Status = False
    ret, frame = spy_video.read() # Function that reads the frames from the actual WebCam.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    fire = spy_fire.detectMultiScale(frame, 1.2, 5) # Functions that detects the fire in frames.

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2) # The function that draws the rectangle that appears on the actual fire.
        roi_gray = gray[y:y+h, x:x+w] # The function that draws the rectangle that appears on the actual fire.
        roi_color = frame[y:y+h, x:x+w] # The function that draws the rectangle that appears on the actual fire.

        if not spy_lock.locked():
            spy_lock.acquire()
            print("######## Spy's Fire Detector™ ########")
            print("github@okspy.codes: Fire detected on the webcam.")
            fire_number = str(len(fire)) # Variable declaration of the fires detected, using the 'len()' function on the 'fire' array.
            print("Fires Detected: " + fire_number)
            threading.Thread(target=spy_play_alarm).start()  # Plays the alarm indexed at line 26.

    cv2.imshow('@okspy47 on GitHub // okspy.codes', frame) # Name of the window.
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Detects the press of the hotkey('Q') and closes the script.
            print("######## Spy's Fire Detector™ ########")
            print("Exiting the program...")
            print("######## Spy's Fire Detector™™ ########")
            break
##################################################################
#                             Runtime
##################################################################