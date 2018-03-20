import cv2
import common

model = cv2.createEigenFaceRecognizer()
model.load(common.TRAINING_FILE)
print 'Training data loaded!'

camera = common.get_camera()
print 'Running Facial Recognizer...'
while True:
    image  = camera.read()
    image  = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    result = common.detect_single(image)
    if result is None:
	print 'Could not detect single face!  Check the image in last_image.pgm' \
	  ' to see what was captured and try again with only one face visible.'
	continue
    x, y, w, h = result
    # Crop and resize image to face.
    crop = face.resize(face.crop(image, x, y, w, h))
    # Test face against model.
    label, confidence = model.predict(crop)
    if label == 1:
        print 'Predicted Rand with Confidence'
        print confidence
    elif label == 2:
        print 'Predicted Ifham with Confidence'
        print confidence
    elif label == 3:
        print 'Predicted Surya with Confidence'
        print confidence
    else:
        print 'Unable to Recognize Face'