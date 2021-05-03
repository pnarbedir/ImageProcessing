import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter

# Open an already existing image
imageObject = Image.open("soru2.jpg");


shr1 = imageObject.filter(ImageFilter.SHARPEN);
shr2 = shr1.filter(ImageFilter.SHARPEN);
shr1.show();
shr2.show();