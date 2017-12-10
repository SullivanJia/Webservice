from PIL import Image

im_path = str('/Users/jiaguanyi/Desktop/WX20171111-003553.png')
im = Image.open(im_path)
im.show()
width, height = im.size
# 宽高
print(str(width)+'    '+str(height))


resizedIm = im.resize((width*2, height*2))
# new.save('/Users/jiaguanyi/Desktop/WX20171111-003553.png')
resizedIm.show()

widths, heights =resizedIm.size
print(str(widths)+'    '+str(heights))
	
