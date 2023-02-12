from PIL import Image

def openImage():
    #opens both images and loads them
    img1 = Image.open("encryptedimg1.png")
    img2 = Image.open("encryptedimg2.png")
    pixels1 = img1.load()
    pixels2 = img2.load()
    width1, height1 = img1.size
    width2, height2 = img2.size

    list1 = []
    #check for correct size
    if width2 != 256 or width1 != 256:
        print("not correct size")

    """
    this part gets the grayscale value of at each pixel of the encrypted images
    Its serves as a coordinate mapping
    Index 0 will have the grayscale value stored as a tuple of the first pixel in image 1 and image 2"""
    for x in range(width1):
        for y in range(height1):
            r1= img1.getpixel((x,y))
            r2= pixels2[x, y]


            list1.append((r1, r2))
    return list1

def rgbToHex(rgb):
    return '%02x%02x%02x' % rgb
def main():

    values = openImage()
    #created image object for making decrypted image.
    finalImage = Image.new(mode="RGB", size=(256, 256))

    #opened flag encrypted image
    img3 = Image.open("encryptedFlag.png")
    img = img3.convert('RGB')
    pixels = img.load()
    width, height = img.size
    counter = 0
    hexlist=""

    """ It gets the value in order of the encrypted image file and puts that pixel in the coordinates indicated
    by the values obtained from the grayscale"""
    for i in range(256):
        for j in range(256):
            finalImage.putpixel((255-values[counter][0], 255-values[counter][1]), pixels[i,j])

            counter += 1

    finalImage.rotate(90).transpose(Image.FLIP_LEFT_RIGHT).show()


if __name__ == '__main__':
    main()