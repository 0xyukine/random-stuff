import os
import re
import cv2

def clean_name(name):
    ex = re.compile(r"([｜])|(![\S]* )|(\[[^\]]*\])|(\.[\S]*)|([^[:ascii:]])") #Purpose specific | Socials (typically kept behind !) | Video ID between brackets | Non-ascii
    name = re.sub(ex, "", name).strip(" ") #Substitute match for null char and trim any remaining whitespace
    return name

def create_directory(name):
    name = clean_name(name).replace(" ", "_")
    try:
        os.mkdir(f"/frames/{name}")
    except FileExistsError as e:
        print("Directory exists")
    except FileNotFoundError as e:
        print("Subdirectory does not exist")

def list_dir(path, desc=""):
    if desc:
        print(desc)
    
    dir_list = os.listdir(path)
    count = 0
    for item in dir_list:
        item = clean_name(item)
        print(f"{count}: {item}")
        count+=1

def get_dir(path):
    
    for dirpath,dirnames,filenames in os.walk(path):
        print(dirpath,dirnames,filenames)

get_dir("/input")

# for item in os.listdir("/input"):
#     create_directory(item)

# list_dir("/videos")
# list_dir("/input", "Input directory:")
# list_dir("/frames")