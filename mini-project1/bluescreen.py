"""
File: bluescreen.py
--------------------
This program shows an example of "greenscreening" (actually
"bluescreening" in this case).  This is where we replace the
pixels of a certain color intensity in a particular channel
(here, we use blue) with the pixels from another image.
"""


from simpleimage import SimpleImage
from PIL import Image

INTENSITY_THRESHOLD = 1.6


def bluescreen(main_filename, back_filename):
    """
    Implements the notion of "bluescreening".  That is,
    the image in the main_filename has its "sufficiently blue"
    pixels replaced with pixel from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "bluescreened" image.
    """
    #image = SimpleImage(main_filename)
    #bg = SimpleImage(back_filename)



    image = Image.open(main_filename).convert("RGB")
    bg = Image.open(back_filename).convert("RGB").resize(image.size)

    out = Image.new("RGB", image.size)

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))

            # Example "is blue?" rule (tune thresholds for your images)
            is_blue = (b > 100) and (b > r + 40) and (b > g + 40)

            if is_blue:
                out.putpixel((x, y), bg.getpixel((x, y)))
            else:
                out.putpixel((x, y), (r, g, b))

    out.save("bluescreen.png")


    # See if this pixel is "sufficiently" blue
    # If so, we get the corresponding pixel from the
    # back image and overwrite the pixel in
    # the main image with that from the back image.
    # Add your code hear
    return out


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    original_stop = SimpleImage('images/11.png')
    original_stop.show()

    original_leaves = SimpleImage('images/2.png')
    original_leaves.show()

    new_img = bluescreen('images/11.png', 'images/2.png')
    new_img.show()


   
if __name__ == '__main__':
    main()
