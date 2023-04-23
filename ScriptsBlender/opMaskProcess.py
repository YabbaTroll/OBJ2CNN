#from PIL import Image, ImageEnhance, ImagePalette

from PIL import Image, ImagePalette
from PIL.Image import core as _imaging
#import PIL.ImagePalette

bw = ImagePalette.ImagePalette('1',[0,0,0,1,1,1])

#modifies image and returns normalized bounding box coords 
def procMask(path):
    
    img = Image.open(path)
    
    w = img.width
    h = img.height
    
    out = img.convert(mode='1',dither = Image.Dither.NONE, palette=bw)
    
    bbP = out.getbbox()
    
    bbox = [bbP[0]/w,bbP[1]/h,bbP[2]/w,bbP[3]/h]
    
    out.save(path)
    
    return(bbox)