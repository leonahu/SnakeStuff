import os

def rename_files():
    #(1) get all file names
    file_list = os.listdir(r"/Users/leonah/Desktop/prank")
    #print(file_list)
    saved_path = os.getcwd()
   
    os.chdir(r"/Users/leonah/Desktop/prank")
    
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789") )
    os.chdir(saved_path)
    
rename_files()
