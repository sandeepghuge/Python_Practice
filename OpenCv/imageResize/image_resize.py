import cv2
import os

images=[]

def getFiles(path):
    for file in os.listdir(path):
        print(file)
        if file.endswith(".jpeg"):
            print("in if")
            images.append(file)


current_root_folder= os.getcwd()
print("Root folder name="+current_root_folder)
project_folder="/OpenCv/imageResize"
input_folder="/inputImage/"
output_folder="/outputImage/"
getFiles(current_root_folder+project_folder+input_folder)
# print("Images",images)

for readImage in images:

    image= cv2.imread(current_root_folder+project_folder+input_folder+readImage)

    # Get original height and width
    print(f"Original Dimensions : {image.shape}")

    # resize image by specifying custom width and height
    print(image.shape[0])
    height= image.shape[0]
    width = image.shape[1]
    updatedHeight= int(height/3)
    updatedWidth= int(width/3)

    #Can't parse 'dsize'. Sequence item with index 0 has a wrong type
    #solution use int casting for this
    resized = cv2.resize(image, (updatedWidth, updatedHeight ))

    print(f"Resized Dimensions : {resized.shape}")
    cv2.imwrite(current_root_folder+project_folder+output_folder+os.path.basename(readImage), resized)




