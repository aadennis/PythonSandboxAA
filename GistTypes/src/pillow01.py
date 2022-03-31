from PIL import Image
import io
import glob
import os

dir = "D:\onedrive\data\photos\_Albums\CameraRollDump\CRD_2021_10"
wildcard = "*ioS.png"
print(dir)
joint = dir + "/" + wildcard

f = glob.glob(joint)
# print(f)

for src_filename in f:

    src_base = os.path.basename(src_filename)
    b = os.path.splitext(src_base)[0]

    target_name = dir + "/" + b + ".jpg"

    print(b)
    print(src_filename)
    print(target_name)

    im = Image.open(src_filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(target_name)

