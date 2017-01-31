#Writing an array to a file:

from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
#plt.show()

#Creating a numpy array from an image file:

from scipy import misc
face = misc.face()
misc.imsave('face.png', face) # First we need to create the PNG file

face = misc.imread('face.png')
type(face)      

#face.shape, face.dtype

#Use matplotlib and imshow to display an image inside a matplotlib figure:
f = misc.face(gray=True)  # retrieve a grayscale image
import matplotlib.pyplot as plt
plt.imshow(f, cmap=plt.cm.gray) 

#Increase contrast by setting min and max values:  
plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200) 
# plt.show()       

# Remove axes and ticks
plt.axis('off')

#Gaussian filter from scipy.ndimage:
from scipy import misc
from scipy.ndimage import gaussian_filter
from PIL import Image

face = misc.face(gray=True)

very_blurred = gaussian_filter(face, sigma=5)
# blurred_face.show()
# very_blurred.show()

face = misc.face(gray = True)
face = misc.imread('face.png')

blurred_face = gaussian_filter(face, sigma=10)

img = Image.fromarray(blurred_face, 'RGB')


# print(type(blurred_face))
img.show()
