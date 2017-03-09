# Shows an image in python window
def showImageFromFile(filename):
	from PIL import Image
	filename.show()

# Shows an image in python window
def showImageFromArr(arr):
	from PIL import Image

	getImagefromArray(arr).show()

# Returns an array after reading an image
def getArrayfromImage(filename):
	from scipy import misc

	return misc.imread(filename)

# Reduces an image size based on the params value and blur type. More the value, more the blurring effect
# blur type 0 shows gaussian blurring whereas 1 shows uniform blurring
def blurring_image(filename, val, blur_type=0):
	from scipy import misc
	from scipy.ndimage import gaussian_filter
	from PIL import Image

	if(blur_type == 0):
		return (gaussian_filter(getArrayfromImage(filename), sigma=val))
	else:
		return uniform_filter(getArrayfromImage(filename), size=val)

# Get an image from an array
def getImagefromArray(arr):
	from PIL import Image
	
	return Image.fromarray(arr)

# Save an image in a directory from an array
def setImagefromArray(arr, filename='data/imageFromArray.png'):
	from PIL import Image
	from scipy import misc

	misc.imsave(filename, arr) # uses the Image module (PIL)

# Get grey image from a certain image
def getGreyImage(filename):
	from scipy import misc
	from PIL import Image

	f = getArrayfromImage(filename)
	return misc.face(gray=True)

# Save a gray image to a directory
def setGreyImage(filename, setname = 'data/grey_image.png'):
	from scipy import misc
	from PIL import Image

	f = getArrayfromImage(filename)
	setImagefromArray(misc.face(gray=True), setname)

# Resize an Image

def resizeImagefromFile(filename, resizeX, resizeY, qualityVal, optimizeVal= True, antialias = True , setname='data/image_scaled.png'):
	from PIL import Image
	foo = Image.open(filename)

	 # Resize the image with an ANTIALIAS filter (gives the highest quality)
	if(antialias == True):
		foo = foo.resize((resizeX, resizeY),Image.ANTIALIAS)
	else:
		foo = foo.resize((resizeX, resizeY))

	foo.save(setname, optimize=optimizeVal, quality=qualityVal)


def resizeImagefromArr(arr, resizeX, resizeY, qualityVal, optimizeVal= True, antialias = True , setname='data/image_scaled.png'):
	from PIL import Image
	x = getImagefromArray(arr)

	 # Resize the image with an ANTIALIAS filter (gives the highest quality)
	foo = x.resize((resizeX, resizeY),Image.ANTIALIAS)
	foo.save(setname, optimize=optimizeVal, quality=qualityVal)


	 

## Implementation

arr = blurring_image('data/face.png', 0)
getImagefromArray(arr)
showImageFromArr(arr)
setImagefromArray(arr)
getGreyImage('data/face.png')
setGreyImage('data/face.png', 'data/grey_image.png')
resizeImagefromFile('data/face.png', 1000, 750, 34, True, False)
resizeImagefromArr(getArrayfromImage('data/face.png'), 1000, 750, 34, True)
