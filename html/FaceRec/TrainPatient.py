import fnmatch
import os
import sys
import select

import cv2
import numpy as np

import common
def walk_files(directory, match='*'):
	"""Generator function to iterate through all files in a directory recursively
	which match the given filename match parameter.
	"""
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)
			
POSITIVE_DIR_R = './training/Rand'
POSITIVE_DIR_I = './training/Ifham'
POSITIVE_DIR_S = './training/Surya'

MEAN_FILE = 'mean.png'
RAND_EI_FILE  = 'rand_eigenface.png'
IFHAM_EI_FILE = 'ifham_eigenface.png'
SURYA_EI_FILE = 'surya_eigenface.png'

print "Reading training images..."
faces = []
labels = []
rand_count  = 0
ifham_count = 0
surya_count = 0

# Read all positive images
for filename in walk_files(POSITIVE_DIR_R, '*.pgm'):
	faces.append(common.prepare_image(filename))
	labels.append(1)
	rand_count += 1
for filename in walk_files(POSITIVE_DIR_I, '*.pgm'):
	faces.append(common.prepare_image(filename))
	labels.append(2)
	ifham_count += 1
for filename in walk_files(POSITIVE_DIR_S, '*.pgm'):
	faces.append(common.prepare_image(filename))
	labels.append(3)
	surya_count += 1

print 'Read', rand_count, 'Rand images and', ifham_count, 'Ifham images.', surya_count, 'Surya images.'
	# Train model
print 'Training model...'
model = cv2.createEigenFaceRecognizer()
model.train(np.asarray(faces), np.asarray(labels))
	# Save model results
model.save(common.TRAINING_FILE)
print 'Training data saved to', common.TRAINING_FILE
	# Save mean and eignface images which summarize the face recognition model.
#mean = model.getMat("mean").reshape(faces[0].shape)
#cv2.imwrite(MEAN_FILE, normalize(mean, 0, 255, dtype=np.uint8))
#eigenvectors = model.getMat("eigenvectors")
#pos_eigenvector = eigenvectors[:,0].reshape(faces[0].shape)
#cv2.imwrite(POSITIVE_EIGENFACE_FILE, normalize(pos_eigenvector, 0, 255, dtype=np.uint8))
#neg_eigenvector = eigenvectors[:,1].reshape(faces[0].shape)
#cv2.imwrite(NEGATIVE_EIGENFACE_FILE, normalize(neg_eigenvector, 0, 255, dtype=np.uint8))

