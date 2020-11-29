import cv2
import os
import time
directory = '/home/evan/huntingApp/videos'
f = open("dateTimeVideo.txt", "w")

# Function to extract frames

count = 0
def FrameCapture(path):
	global count
	# Path to video file
	vidObj = cv2.VideoCapture(path)
	framerate = vidObj.get(cv2.CAP_PROP_FRAME_COUNT)
	# Used as counter variable
	# checks whether frames were extracted
	success = 1
	# vidObj object calls read
	# function extract frames
	success, image = vidObj.read()
	# Saves the frames with frame-count
	if success == 1:
		cv2.imwrite("frame%d.jpg" % (count), image)
	count += 1
	

# Driver Code
if __name__ == '__main__':
	# Calling the function
	for entry in os.scandir(directory):
		if(entry.path.endswith(".mp4")):
			f.write("%s \n" % time.ctime(os.path.getmtime(entry)))
			FrameCapture(str(entry.path))
			#Save single frame from each video
	f.close()

	
