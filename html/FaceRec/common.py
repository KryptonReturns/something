
import cv2

# Face detection cascade classifier configuration.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html

POSITIVE_DIR = './training/positive'
NEGATIVE_DIR = './training/negative'

POSITIVE_LABEL = 1
NEGATIVE_LABEL = 2

HAAR_FACES         = 'haarcascade_frontalface_alt.xml'
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

FACE_WIDTH  = 92
FACE_HEIGHT = 112

POSITIVE_FILE_PREFIX = 'positive_'
POSITIVE_THRESHOLD = 2000.0
TRAINING_FILE = 'training.xml'

haar_faces = cv2.CascadeClassifier(HAAR_FACES)

def get_camera():
	import picam
	return picam.OpenCVCapture()

def detect_single(image):
	"""Return bounds (x, y, width, height) of detected face in grayscale image.
	   If no face or more than one face are detected, None is returned.
	"""
	faces = haar_faces.detectMultiScale(image, 
				scaleFactor=HAAR_SCALE_FACTOR, 
				minNeighbors=HAAR_MIN_NEIGHBORS, 
				minSize=HAAR_MIN_SIZE, 
				flags=cv2.CASCADE_SCALE_IMAGE)
	if len(faces) != 1:
		return None
	return faces[0]

def crop(image, x, y, w, h):
	"""Crop box defined by x, y (upper left corner) and w, h (width and height)
	to an image with the same aspect ratio as the face training data.  Might
	return a smaller crop if the box is near the edge of the image.
	"""
	crop_height = int((FACE_HEIGHT / float(FACE_WIDTH)) * w)
	midy = y + h/2
	y1 = max(0, midy-crop_height/2)
	y2 = min(image.shape[0]-1, midy+crop_height/2)
	return image[y1:y2, x:x+w]

def resize(image):
	"""Resize a face image to the proper size for training and detection.
	"""
	return cv2.resize(image, 
					  (FACE_WIDTH, FACE_HEIGHT), 
					  interpolation=cv2.INTER_LANCZOS4)
					  
def walk_files(directory, match='*'):
	"""Generator function to iterate through all files in a directory recursively
	which match the given filename match parameter.
	"""
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

def prepare_image(filename):
	"""Read an image as grayscale and resize it to the appropriate size for
	training the face recognition model.
	"""
	return resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

def normalize(X, low, high, dtype=None):
	"""Normalizes a given array in X to a value between low and high.
	Adapted from python OpenCV face recognition example at:
	  https://github.com/Itseez/opencv/blob/2.4/samples/python2/facerec_demo.py
	"""
	X = np.asarray(X)
	minX, maxX = np.min(X), np.max(X)
	# normalize to [0...1].
	X = X - float(minX)
	X = X / float((maxX - minX))
	# scale to [low...high].
	X = X * (high-low)
	X = X + low
	if dtype is None:
		return np.asarray(X)
	return np.asarray(X, dtype=dtype)
	