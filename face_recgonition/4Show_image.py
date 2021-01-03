#/usr/bin/env python2.7


from PIL import Image
import numpy 
import  cv2

# wIndos to disply image 
cv2.namedWindow("Image")


#read image 

image = cv2.imread('/home/devloper-pratthamesh/Desktop/Screenshot from 2020-05-27 15-50-16.png')
h,w = image.shape[:2]
print(h,w)

#save image 

cv2.imwrite('/home/devloper-pratthamesh/Desktop/result.png',image)

#show image 

cv2.imshow("Image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()




