import cv2
import face_recognition
import pickle
import os

# Importing the student images
folderPath = 'images'
pathList = os.listdir(folderPath)
print(pathList)

imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 0:  # Check if a face is detected
            encode = encodings[0]
            encodeList.append(encode)
        else:
            print("Warning: No face detected in an image. Skipping that image.")

    return encodeList


print("Encoding Started....")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save the encodings and IDs to a file
with open("EncodeFile.p", "wb") as file:
    pickle.dump(encodeListKnownWithIds, file)
print("File Saved")
