import cv2,os
from PIL import Image
print(os.getcwd())
os.chdir("C:/Users/codin/Pictures/Jetlearn")
p="C:/Users/codin/Pictures/Jetlearn"
meanheight=0
meanwidth=0
noi=len(os.listdir(p))
print(noi)
for i in os.listdir('.'):
    img=Image.open(os.path.join(p,i))
    width,height=img.size
    meanwidth+=width
    meanheight+=height
meanheight=int(meanheight/noi)
meanwidth=int(meanwidth/noi)
for i in os.listdir('.'):
    if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg"):
        img=Image.open(os.path.join(p,i))
        width,height=img.size
        r=img.resize((width,height))
        r.save(i,"jpeg",quality=97)
        print(img.filename.split("\\")[-1]," is resized")
def genvideo():
    imgb="."
    videoname="Blah.avi"
    os.chdir(p) 
    img=[t for t in os.listdir(imgb)
         if t.endswith(".jpeg") or t.endswith(".jpg") or t.endswith(".png")]
    print(img)
    d=cv2.imread(os.path.join(imgb,img[0]))
    height,width,layers=d.shape
    video=cv2.VideoWriter(videoname,0,1,(width,height))
    for image in img:
        video.write(cv2.imread(os.path.join(imgb,image)))
    cv2.destroyAllWindows()
    video.release()
genvideo()
