import os
from PIL import Image

yourpath = os.getcwd()
for root, dirs, files in os.walk(yourpath, topdown=False):
	for name in files:
		#print(os.path.join(root, name))
		if (os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff") or (os.path.splitext(os.path.join(root, name))[1].lower() == ".gif") or (os.path.splitext(os.path.join(root, name))[1].lower() == ".jpg"):

			outfile = os.path.splitext(os.path.join(root, name))[0] + ".png"
			print len(outfile)
			try:
				im = Image.open(os.path.join(root, name))
				print ("Generating png for %s" % name)
				im.thumbnail(im.size)
				im.convert('RGB').save(outfile, "PNG", optimize=True)
				os.remove(os.path.join(root, name))
			except KeyError:
				pass
