import sys, os;
file_path = "Pillow-master";
sys.path.append( os.path.dirname( file_path ) );

from functions import *

from PIL import Image;
from PIL import ImageShow;

img = Image.open("cm3MIMc.png");

#select a tile from the image
#find starting and end points and feed it to this
T = get_tile(img, 441,23,483,43);
# ImageShow.show(T);

n = get_similar_tile_count(img, T);
print(n);