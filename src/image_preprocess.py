# create variables image from source
# Source: https://pillow.readthedocs.io/en/3.0.x/reference/ImageOps.html
from PIL import ImageOps, Image
from io import BytesIO


class ImagePreProccess:
    def __init__(self, path_to_image="", image=None):
        try:
            if(image != None):
                self.img  = image
            else:
                self.img = Image.open(path_to_image)

            width, height = self.img.size
            self.width = width
            self.height = height
        except:
            print(f"Cannot open image at path: {path_to_image}")

    def crop(self, left, up, right, bottom):
        border = (left, up, right, bottom)
        return ImageOps.crop(self.img, border)

    def autocontrast(self, cutoff=0, ignore=None):
        return ImageOps.autocontrast(self.img, cutoff, ignore)

    def colorize(self, black, white):
        return ImageOps.colorize(self.img, black, white)

    def deform(self, deformer, resample=2):
        return ImageOps.deform(self.img, deformer, resample)

    def equalize(self, mask=None):
        return ImageOps.equalize(self.img, mask=None)

    def expand(self, border=0, fill=0):
        return ImageOps.expand(self.img, border, fill)

    def fit(self, size, method=0, bleed=0.0, centering=(0.5, 0.5)):
        return ImageOps.fit(self.img, size, method, bleed, centering)

    def flip(self):
        return ImageOps.flip(self.img)

    def grayscale(self):
        return ImageOps.grayscale(self.img)

    def invert(self):
        return ImageOps.invert(self.img)

    def mirror(self):
        return ImageOps.mirror(self.img)

    def posterize(self, bits):
        return ImageOps.posterize(self.img, bits)

    def solarize(self, threshold=128):
        return ImageOps.solarize(self.img, threshold)

    def toJPG(self):
        self.img.convert('RGB')
        faux_file = BytesIO()
        self.img.save(faux_file, 'jpeg')
        return Image.open(faux_file)

    def toPNG(self):
        self.img.convert('RGB')
        faux_file = BytesIO()
        self.img.save(faux_file, 'png')
        return Image.open(faux_file)
    
    def toGIF(self):
        self.img.convert('L')
        faux_file = BytesIO()
        self.img.save(faux_file, 'gif')
        return Image.open(faux_file)

    def origin(self):
        return self.img