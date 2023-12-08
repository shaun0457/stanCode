"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_dis = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_dis # 距離



def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    p_red = 0
    p_green = 0
    p_blue = 0
    p_list = []
    for i in range(len(pixels)):
        p_red += pixels[i].red
        p_blue += pixels[i].blue
        p_green += pixels[i].green
    p_red_avg = p_red // len(pixels)
    p_list += [p_red_avg]
    p_green_avg = p_green // len(pixels)
    p_list += [p_green_avg]
    p_blue_avg = p_blue // len(pixels)
    p_list += [p_blue_avg]

    return p_list #RGB平均的list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    best_pixel = 300
    best_pixel1 = []
    g_a = get_average(pixels)
    for i in range(len(pixels)):
        pixel_dis = get_pixel_dist(pixels[i], g_a[0], g_a[1], g_a[2]) # pixel dis(int) n顆Pixel
        if pixel_dis < best_pixel:
            best_pixel = pixel_dis
            best_pixel1 = pixels[i]

    return best_pixel1



def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # M4
    # list = []
    # for x in range(width):
    #     for y in range(height):
    #         for k in range(len(images)):
    #             list += images[k]
    #         get_best_pixel(list)
            # print(get_best_pixel(list))

    for x in range(width):
        for y in range(height):
            list_pixel = []
            for img in images:
                list_pixel.append(img.get_pixel(x, y))
            best1 = get_best_pixel(list_pixel)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best1.red
            result_pixel.green = best1.green
            result_pixel.blue = best1.blue



    # M3
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel(([green_pixel, blue_pixel, blue_pixel]))
    # print(green_pixel)
    # print(best1.red, best1.green, best1.blue)

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
