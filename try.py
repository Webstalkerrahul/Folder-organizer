import shutil
import glob
import os

# Base directories to store
Base_path='Your Folder path'
file_names = glob.glob(Base_path+"*")


def arrage(Base_path,file_list):
    # Empty list to store related file names
    img=[]
    docs=[]
    programs=[]
    software=[]
    video=[]

    #Formats to sperated file types basically sorting img, docs, etc 
    img_types=(".jpg" , ".png" , ".jpeg", ".svg", ".webp", ".jfif")
    doc_types=(".pdf",".PDF" , ".csv" , ".xlxs" , ".doc" , ".docx" , ".txt" , ".pptx",".json",".torrent",".xlsx",".ai",".eps")
    pro_types=(".c" , ".py" , ".js" , ".xml" , ".ipynb" , ".html" , ".css" , ".cms",".sql",".sqlite",".class")
    software_types=(".exe" , ".msi" , ".zip" , ".rar",".7z",".jar")
    vid_types=(".mp4" , ".mov" , ".gif" , "vid" , ".mkv")

    #Filenames will be stored in here according to types mentioned above
    for file in file_list:
        if file.endswith(img_types):
            img.append(file)
        
        elif file.endswith(doc_types):
            docs.append(file)

        elif file.endswith(pro_types):
            programs.append(file)
        
        elif file.endswith(software_types):
            software.append(file)
        
        elif file.endswith(vid_types):
            video.append(file)
        
    #Loop for the names to make folder according to the types and moving the files     
    for i in img:
        try:
            os.makedirs(Base_path+'images')
            shutil.move(i,Base_path+"images")
        except FileExistsError:
            shutil.move(i,Base_path+"images")
    
    for i in docs:
        try:
            os.makedirs(Base_path+'documents')
            shutil.move(i,Base_path+"documents")
        except FileExistsError:
            shutil.move(i,Base_path+"documents")
    
    for i in programs:
        try:
            os.makedirs(Base_path+'programs')
            shutil.move(i,Base_path+"programs")
        except FileExistsError:
            shutil.move(i,Base_path+"programs")
    
    for i in software:
        try:
            os.makedirs(Base_path+'software')
            shutil.move(i,Base_path+"software")
        except FileExistsError:
            shutil.move(i,Base_path+"software")
    
    for i in video:
        try:
            os.makedirs(Base_path+'vidoes')
            shutil.move(i,Base_path+"vidoes")
        except FileExistsError:
            shutil.move(i,Base_path+"vidoes")

arrage(Base_path,file_names)