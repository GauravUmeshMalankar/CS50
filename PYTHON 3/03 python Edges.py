from PIL import Image,ImageFilter

before=Image.open("bridge.jpg")
after=before.filter(ImageFilter.FIND_EDGES)
after.save("out2.jpg")
