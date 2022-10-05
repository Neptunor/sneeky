import cv2

img = cv2.imread('/Users/jiaqi/Desktop/code/sneeky/beach.png')

img2 = cv2.imread('/Users/jiaqi/Desktop/code/sneeky/beach2.png)')

newImg = cv2.hconcat([img, img2])

cv2.imshow("Martin", newImg)

cv2.waitKey(0)


