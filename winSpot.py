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
		with Image.open(filename) as img:
			width, height = img.size
		newfile = cwd + "\\" + str(foldername) + "\\" + str(n) + ".jpg"
		shutil.copy(dir + "\\" + filename, newfile)
		n += 1

main()