"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    final_image = put_patch(final_image, 0, 0, patch)

    patch1 = make_recolored_patch(0, 1, 0)
    final_image = put_patch(final_image, patch.width, 0, patch1)

    patch2 = make_recolored_patch(0, 0, 1)
    final_image = put_patch(final_image, patch.width * 2, 0, patch2)

    patch3 = make_recolored_patch(1, 1, 1)
    final_image = put_patch(final_image, 0, patch2.height, patch3)

    patch4 = make_recolored_patch(0, 1.5, 1.5)
    final_image = put_patch(final_image, patch4.width, patch4.height, patch4)

    patch5 = make_recolored_patch(0.5, 0.5, 0)
    final_image = put_patch(final_image, patch5.width * 2, patch5.height, patch5)
    final_image.show()


def put_patch(final_image, start_x, start_y, patch):
    for x in range(patch.width):
        for y in range(patch.height):
            final_image.set_pixel(start_x + x, start_y + y, patch.get_pixel(x, y))
    return final_image


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch


if __name__ == '__main__':
    main()