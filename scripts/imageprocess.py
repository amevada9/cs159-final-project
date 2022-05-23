# importing the necessary libraries
import cv2
import numpy as np

#name of the video here
filename = 'stevetest'
#if it's not in a .MOV extension, just change the next part
cap = cv2.VideoCapture(filename + '.MOV')

#folder for the pitches - like fastball or curveball or something - this is where
folder = 'testfolder'

#this number is the last n frames of the video that we care about.  Like the last 3 
#frames here offer good images
frames = 4

#------fill in all the items above-----

#-------everything below doesn't need to be edited unless you run into issues.  I did it a little jank
#------- but I think it should work 

#literally just need to count how many frames there are and for some reason I need to loop 
count = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    count += 1

# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv2.destroyAllWindows()



#now we actually do some stuff with it - saves the last n images into desired folder.
cap = cv2.VideoCapture(filename + '.MOV')
count2 = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    count2 += 1
    if count2 > count - frames:
        cv2.imwrite(folder + 'filename' + str(count2-count+frames) + '.jpg', frame)

# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv2.destroyAllWindows()

