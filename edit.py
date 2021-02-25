from image import Image
import numpy as np

def adjust_brightness(image, factor):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = image.array[x,y,c]*factor
    
    # new_im.array = image.array*factor
    return new_im

def adjust_contrast(image,factor,mid=0.5):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x,y,c] = (image.array[x,y,c]-mid)*factor + mid
    new_im.array = (image.array-mid)*factor + mid
    return new_im

def blur(image, kernel_size):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    neighbour_range = kernel_size//2
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbour_range), min(x_pixels-1,x+neighbour_range)+1):
                    for y_i in range(max(0,y-neighbour_range), min(y_pixels-1,y+neighbour_range)+1):
                        total += image.array[x_i, y_i, c] 
                new_im.array[x,y,c] = total / (kernel_size**2)
                #new_im.array[x,y,c] = (image.array[x,y,c])
    return new_im

def apply_kernel(image, kernel):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    kernel_size = kernel.shape[0]
    neighbour_range = kernel_size//2
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbour_range), min(x_pixels-1,x+neighbour_range)+1):
                    for y_i in range(max(0,y-neighbour_range), min(y_pixels-1,y+neighbour_range)+1):
                        x_k = x_i + neighbour_range - x
                        y_k = y_i + neighbour_range - y
                        kernel_val = kernel[x_k,y_k]
                        total += image.array[x_i,y_i,c]*kernel_val
                new_im.array[x,y,c] = total
    
    return new_im

def combine_image(image1, image2):
    x_pixels, y_pixels, num_channels = image1.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = (image1.array[x,y,c]**2 + image2.array[x,y,c]**2)**0.5
    return new_im

def india_flag(image):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                if x < (x_pixels//3):
                    if c == 0:
                        new_im.array[x,y,c] = image.array[x,y,c]
                    if c == 1:
                        new_im.array[x,y,c] = image.array[x,y,c]*0.6
                    if c == 2:
                        new_im.array[x,y,c] = image.array[x,y,c]*0.2
                if x >= (x_pixels//3) and x < (2*x_pixels//3):
                    if c == 0:
                        new_im.array[x,y,c] = image.array[x,y,c]*4
                    if c == 1:
                        new_im.array[x,y,c] = image.array[x,y,c]*4
                    if c == 2:
                        new_im.array[x,y,c] = image.array[x,y,c]*4
                if x >= (2*x_pixels//3) and x <= (x_pixels):
                    if c == 0:
                        new_im.array[x,y,c] = image.array[x,y,c]*1
                    if c == 1:
                        new_im.array[x,y,c] = image.array[x,y,c]*4
                    if c == 2:
                        new_im.array[x,y,c] = image.array[x,y,c]*1

                # if c<2:
                #     new_im.array[x,y,c] = image.array[x,y,c]
                # else:
                #     new_im.array[x,y,c] = image.array[x,y,c]*2

                # if new_im.array[x,y,c] <=0.3:
                #     new_im.array[x,y,c] = 0
                # elif new_im.array[x,y,c] <=0.6:
                #     new_im.array[x,y,c] = 0.3
                # elif new_im.array[x,y,c] <=0.9:
                #     new_im.array[x,y,c] = 0.5
                # else:
                #     new_im.array[x,y,c] = 1
    return new_im

def invert_image(image):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = 0.5-image.array[x,y,c]
    return new_im

def warmth(image):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            new_im.array[x,y,0] = image.array[x,y,0]
            new_im.array[x,y,1] = image.array[x,y,1]*.27
            new_im.array[x,y,2] = image.array[x,y,2]*0
                
    return new_im

def weird(image):
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            new_im.array[x,y,0] = image.array[x,y,0]
            new_im.array[x,y,1] = image.array[x,y,1]
            new_im.array[x,y,2] = image.array[x,y,2]
            if new_im.array[x,y,0]**2 + new_im.array[x,y,1]**2 + new_im.array[x,y,2]**2 == 3:
                new_im.array[x,y,0] = image.array[x,y,0]*2
    return new_im

if __name__=="__main__":
    # field = Image(filename='field.png')
    # car = Image(filename='car1.png')
    shashi = Image(filename='shashi.png')

    # brightened_im = adjust_brightness(shashi,2)
    # brightened_im.write_image('brightened_shashi.png')
    # darkened_im = adjust_brightness(field,0.1)    
    # darkened_im.write_image('darkened2.png')
    # contrast_im = adjust_contrast(field,0.7)
    # contrast_im.write_image('contrasted4.png')
    # blurred_im = blur(field,10)
    # blurred_im.write_image('blurred4.png')

    # sobel_x_kernel = np.array([
    #     [1,2,1],
    #     [0,0,0],
    #     [-1,-2,-1]
    # ])
    # sobel_y_kernel = np.array([
    #     [1,0,-1],
    #     [2,0,-2],
    #     [1,0,-1]
    # ])

    # sobel_x = apply_kernel(shashi, sobel_x_kernel)
    # sobel_x.write_image('edge_x.png')
    # sobel_y = apply_kernel(shashi, sobel_y_kernel)
    # sobel_y.write_image('edge_y.png')

    # edge_xy = combine_image(sobel_x, sobel_y)
    # edge_xy.write_image('edge_xy2.png')
    # flag = india_flag(shashi)
    # flag.write_image('grayed9.png')
    # inverted = invert_image(shashi)
    # inverted.write_image('inverted2.png')

    # warmed = warmth(shashi)
    # warmed.write_image('warmed.png')

    weirder = weird(shashi)
    weirder.write_image('weirder2.png')