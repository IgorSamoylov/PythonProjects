import os
from PIL import Image

class ImageConverter:
    
    def convert_file(old_file, extension=".webp", new_ext=".jpg"):
        img = Image.open(old_file).convert("RGB")
        new_file_name = old_file.replace(extension, new_ext, 1)
        img.save(new_file_name, "jpeg")
        print(new_file_name + " converted and saved")
        os.remove(old_file)
        
    def convert_dir(path, new_path, extension=".webp", new_ext=".jpg"):

        for path, dir_list, files_list in os.walk(path):
            
            for file in files_list:
                
                if file.endswith(extension):
                    
                    old_file = os.path.join(path, file)
                    img = Image.open(old_file).convert("RGB")
                    new_file_name = file.replace(extension, new_ext, 1)
                    try:
                        img.save(os.path.join(new_path, new_file_name), "jpeg") # must be jpeg not jpg!
                        os.remove(old_file)
                    except RuntimeException as ex:
                        print("Error " + ex)
                    else:
                        print(new_file_name + " converted and saved")
                        
        print("All files has been converted succefully!")

#path = "C:/Users/A12/Downloads/PICTURES"
#ImageConverter.image_converter(path, path)
