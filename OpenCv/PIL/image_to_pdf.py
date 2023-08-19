
import os
from PIL import Image
current_root_folder= os.getcwd()
print("Root folder name="+current_root_folder)
project_folder="/OpenCv/PIL"
input_image_folder="/inputImage/"
output_image_folder="/outputFiles/"
image_1 = Image.open(current_root_folder+project_folder+input_image_folder+'1.jpeg')
im_1 = image_1.convert('RGB')
im_1.save(current_root_folder+project_folder+output_image_folder+"output.pdf")