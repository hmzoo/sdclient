import base64                                                                                                                         
from PIL import Image

def fmtpng(t,n):
  return "{:s}_{:04d}".format(t,i)

def saveimg(bimg,fdir,fname):
    image = Image.open(io.BytesIO(base64.b64decode(bimg)))                                                                      
    image.save(fname)


for i in range(6):
    ind=fmtpng("img",i)
    print(ind)