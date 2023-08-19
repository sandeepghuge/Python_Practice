
import os
from PIL import Image
images=[]

def getFiles(path):
    for file in os.listdir(path):
        print(file)
        if file.endswith(".jpeg"):
            print("in if")
            images.append(file)


current_root_folder= os.getcwd()
print("Root folder name="+current_root_folder)
project_folder="/OpenCv/PIL/image_to_pdf"
input_folder="/inputImage/"
output_folder="/outputFiles/"

image_list=[]
getFiles(current_root_folder+project_folder+input_folder)

for readImage in images:
    image=Image.open(current_root_folder+project_folder+input_folder+readImage,"r")
    imageObject=image.convert('RGB')
    image_list.append(imageObject)


image_list[0].save(current_root_folder+project_folder+output_folder+"output.pdf", save_all=True, append_images=image_list[1:])