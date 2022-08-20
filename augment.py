import os

import cv2
import numpy as np
import random
import glob


def save(list_of_pics, path):

    for i in range(len(list_of_pics)):
        x = random.randint(0,999)
        cv2.imwrite(os.path.join(path, f'pic{x}.jpg'), list_of_pics[i])


def scaler(img_path, number):
    img=cv2.imread(img_path)
    sowar = []
    for i in range(number):
        ffx=random.uniform(0, 4)
        ffy=random.uniform(0, 4)
        sowar.append(
            cv2.resize(img, None, fx=ffx, fy=ffy, interpolation=cv2.INTER_AREA))
        cv2.imshow(f"scale{ffx}x{ffy}", sowar[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return sowar


def zoom(img_path, number):
    sowar = []
    img = cv2.imread(img_path)
    for i in range(number):
        f = random.uniform(0, 10)
        sowar.append(
            cv2.resize(img, None, fx=f, fy=f, interpolation=cv2.INTER_AREA))
        cv2.imshow(f"zoom{f}", sowar[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return sowar


def translate_img(image_trans_path, number):
    image_trans=cv2.imread(image_trans_path)
    height = image_trans.shape[0]
    width = image_trans.shape[1]
    pics = []
    for i in range(number):
        w=random.randrange(0, width //2, 30)
        h=random.randrange(0, height //2, 30)
        transMatx = np.float32(
            [[1, 0, w], [0, 1,h ]])
        dimensions = (width, height)
        pics.append(cv2.warpAffine(image_trans, transMatx, dimensions))
        cv2.imshow(f"Translated image {w}X{h}", pics[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return pics


def rotation(image_rotate_path, number):
    image_rotate=cv2.imread(image_rotate_path)
    (h, w) = image_rotate.shape[:2]
    center = (w // 2, h // 2)
    pics = []
    for i in range(number):
        angle=random.randrange(0, 360, 10)
        rotationmatrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        pics.append(cv2.warpAffine(image_rotate, rotationmatrix, (w, h)))
        cv2.imshow(f"rotation,{angle}", pics[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return pics


def cropping(image_crop_path, number):
    image_crop=cv2.imread(image_crop_path)
    pics = []
    (h, w) = image_crop.shape[:2]
    for i in range(number):
        pics.append(image_crop[random.randrange(0, h // 2, 10):random.randrange(h // 2, h, 10),
                    random.randrange(0, w // 2, 10):random.randrange(w // 2, w, 10)])
        cv2.imshow(f"crop{i}", pics[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return pics


def contrast(image_contrast_path, number):
    image_contrast=cv2.imread(image_contrast_path)
    pics_contrast = []
    cv2.imshow('Original Image', image_contrast)
    for i in range(number):
        alfa=random.randrange(1, 50, 10)
        contrast_img = cv2.addWeighted(image_contrast, alfa,
                                       np.zeros(image_contrast.shape, image_contrast.dtype), 0, 0)
        pics_contrast.append(contrast_img)
        cv2.imshow(f'Contrast Image{alfa}', pics_contrast[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return pics_contrast


def brightness(image_bright_path, number):
    image_bright=cv2.imread(image_bright_path)
    pics_bright = []
    cv2.imshow('Original Image', image_bright)
    for i in range(number):
        beta=random.randrange(-127, 127, 10)
        brightness_img = cv2.addWeighted(image_bright, 1, np.zeros(image_bright.shape, image_bright.dtype), 0,
                                         beta)
        pics_bright.append(brightness_img)
        cv2.imshow(f'brightness Image{beta}', pics_bright[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return pics_bright

def blur(image_blur_path,number):
    image_blur=cv2.imread(image_blur_path)
    (h,w)=image_blur.shape[:2]
    pics_blurred=[]
    cv2.imshow('Blurred image',image_blur)

    for i in range(number):
        blurfactor=random.randrange(0,20,2)
        smooth = cv2.bilateralFilter(image_blur, blurfactor, h, w)
        pics_blurred.append(smooth)
        cv2.imshow(f'blurred image{blurfactor}',smooth)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return pics_blurred


