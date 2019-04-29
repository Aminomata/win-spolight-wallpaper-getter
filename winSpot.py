import os
import shutil
from PIL import Image

foldername = "WinSpotFiles"


def makeFolder():
    cwd = os.getcwd()
    dir = cwd + "\\" + foldername
    if not os.path.exists(dir):
        os.makedirs(dir)


def main():
    makeFolder()
    homedir = os.environ['HOMEPATH']
    dir = homedir + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    n = 0
    for filename in os.listdir(dir):
        cwd = os.getcwd()

        try:
            with Image.open(dir + "\\" + filename) as img:
                width, height = img.size
        except:
            continue

        if height == 1080 and width == 1920:
            print("test1")
            newfile = cwd + "\\" + str(foldername) + "\\" + str(n) + ".jpg"
        elif height == 1920 and width == 1080:
            print("test2")
            newfile = cwd + "\\" + str(foldername) + "\\" + str(n) + ".jpg"
        else:
            continue

        shutil.copy(dir + "\\" + filename, newfile)
        n += 1


main()
