import cv2
import os

current_root_folder= os.getcwd()
print("Root folder name="+current_root_folder)
project_folder="/OpenCv/imageResize"
input_folder="/inputImage/"
output_folder="/outputImage/"
image= cv2.imread(current_root_folder+project_folder+input_folder+"1.jpeg")

# Get original height and width
print(f"Original Dimensions : {image.shape}")

# resize image by specifying custom width and height
print(image.shape[0])
height= image.shape[0]
width = image.shape[1]
updatedHeight= int(height/2)
updatedWidth= int(width/2)

#Can't parse 'dsize'. Sequence item with index 0 has a wrong type
#solution use int casting for this
resized = cv2.resize(image, (updatedWidth, updatedHeight ))

print(f"Resized Dimensions : {resized.shape}")
cv2.imwrite(current_root_folder+project_folder+output_folder+'resized_imaged.jpg', resized)

