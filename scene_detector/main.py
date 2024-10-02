import os
import re
import cv2

def list_dir(path, desc=""):
    if desc:
        print(desc)
    
    dir_list = os.listdir(path)
    count = 0
    for item in dir_list:
        ex = re.compile(r"([｜])|(![\S]* )|(\[[^\]]*\])|(\.[\S]*)|([^[:ascii:]])") #Purpose specific | Socials (typically kept behind !) | Video ID between brackets | Non-ascii
        item = re.sub(ex, "", item).strip(" ") #Substitute match for null char and trim any remaining whitespace
        print(f"{count}: {item}")
        count+=1

list_dir("/videos")
list_dir("/input", "Input directory:")