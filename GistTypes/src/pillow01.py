from PIL import Image
import io
import glob
import os

dir = "D:\onedrive\data\photos\_Albums\CameraRollDump\CRD_2021_10"
wildcard = "*ioS.png"
print(dir)
joint = dir + "/" + wildcard

f = glob.glob(joint)
#print(f)

for i in f:
   print(i)
   a = os.path.basename(i)
   b = os.path.splitext(a)[0]

   print(b)


# im = Image.open("a.png")
# rgb_im = im.convert('RGB')
# rgb_im.save('b.jpg')




