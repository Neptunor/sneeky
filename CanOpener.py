import cv2
import numpy as np

# img = cv2.imread('/Users/jiaqi/Desktop/code/sneeky/beach.png')

# img2 = cv2.imread('/Users/jiaqi/Desktop/code/sneeky/beach2.png)')

img = np.zeros((512,512,3), np.uint8)

# newImg = cv2.hconcat([img, img2])

cv2.line(img,(50,400),(461,400),(255,0,0),5)

cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.circle(img,(63,63), 63, (0,0,255), -1)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.rectangle(img,(0,0),(126,128),(0,255,0),3)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

cv2.imshow("Martin", img)

cv2.waitKey(0)




