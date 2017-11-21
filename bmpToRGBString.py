from PIL import Image
im = Image.open("C:\Users\dinet\Documents\poopEmoji.bmp") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
print im.size[0]
colors = im.getcolors()
for color in colors:
	print color
width = int(im.size[0])
height = int(im.size[1])
rows = []
rowString = ""
for y in range(0,height):
	#rowString = ""
	for x in range(0,width):
		rowString += str(pix[x,y]) + "," #Get the RGBA Value of the a pixel of an image
		#pix[x,y] = value # Set the RGBA Value of the image (tuple)
	rows.append(rowString);
#for row in rows:
	#theString = row
	#theString = theString.replace("),(",".")
	#theString = theString.replace("(","")
	#theString = theString.replace(")","")
	#print 'stringList.add("'+theString+'");'
print rowString