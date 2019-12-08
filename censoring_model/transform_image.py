from PIL import Image
import os
import argparse

def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory + img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory + img)
        print("> Image " + img + " is successfully resized")
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Target image size')
    args = parser.parse_args()
    rescale_images(args.directory, args.size)
    print("> Script is completed")