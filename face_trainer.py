import os
import numpy as np
from PIL import Image
import cv2


path = 'Pictures/face'
cascadePath = "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.createLBPHFaceRecognizer()
basewidth = 500


def get_images_and_lables(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    for image_path in image_paths:
        try:
            pilImage = Image.open(image_path).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            ID = int(os.path.split(image_path)[-1].split('.')[1])
            # print ID
            faces = detector.detectMultiScale(imageNp, 1.2, 5)

            for (x, y, w, h) in faces:
                # cv2.rectangle(imageNp, (x, y), (x + w, y + h), (255, 0, 255), 2)
                crop = imageNp[y:y + h, x:x + w].copy()
                # cv2.rectangle(crop, (x, y), (x + w, y + h), (0, 0, 255), 2)
                faceSamples.append(crop)
                Ids.append(ID)
                # cv2.imshow("Training", imageNp)
                cv2.imshow("Cropped", crop)
                cv2.waitKey(300)
        except IOError:
            print '%s could not be opened' % image_path

    return faceSamples, Ids

faces, Ids = get_images_and_lables('Pictures/face')
recognizer.train(faces, np.array(Ids))
print np.array(Ids)
recognizer.save('recognizer/trainingData.yml')
