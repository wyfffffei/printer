from PIL import Image
import numpy as np


def rotate_pic(img):
    """
    @ func @  roate picture to (w >= h)
    """
    w, h = img.size
    if w >= h:
        return None
    
    img_array = np.asarray(img)
    img_array = np.rot90(img_array, 1)
    img = Image.fromarray(img_array)
    return img


def padding_pic(img):
    """
    @ func: add padding from rectangle to square picture (w > h)
    """
    w, h = img.size
    if w <= h:
        return None
    padding = (h - w) // 2
    img_padded = np.zeros(shape=(h, h, 3), dtype=np.uint8)  # 创建正方形矩阵
    img_padded[:, padding:padding+w, :] = img               # 将图片填入矩阵
    img_array = np.rot90(img_padded, 1)                     # 逆时针旋转矩阵 90 度
    img = Image.fromarray(img_array)                        # 矩阵转换回 Pillow 对象
    return img


def more_padding_pic(img):
    """
    @ func: add padding with random color
    """
    ori_size = (1024, 1024)
    new_size = (1366, 768)
    img.thumbnail(new_size, Image.Resampling.LANCZOS)
    padding = abs(new_size[0] - new_size[1]) // 2

    # 创建底板
    img_padded = np.zeros(shape=(new_size[1], new_size[0], 3), dtype=np.uint8)
    img_padded[:, padding: padding + new_size[1], :] = img

    # 填充颜色
    # padding_content = 255 * np.ones((new_size[1], padding, 3), dtype=np.uint8)  # 白色
    padding_content = 255 * np.random.randint((new_size[1], padding, 3))          # 随机颜色
    
    # 填充颜色
    img_padded[:, :padding, :] = padding_content
    img_padded[:, padding + 768:, :] = padding_content
    
    new_img = Image.fromarray(img_padded)
    return new_img


def reg_pic(pictures, path, config):
    """
    @ func @  regulate pictures
    """

    width = config["width"]
    height = config["height"]
    w_margin = config["w_margin"]
    h_margin = config["h_margin"]
    
    if not pictures:
        return None
        
    # image1 = Image.open("{}/1.jpg".format(path)).resize((width, height))
    for idp, picture in enumerate(pictures):
        image = Image.open("{}/{}".format(path, picture))
        if idp == 0:
            new_image = Image.new('RGB', (2 * (w_margin + width), 2 * (h_margin + height)), 'white')
        if image.size[0] < image.size[1]:
            image = rotate_pic(image)
        image.thumbnail((width, height), Image.Resampling.LANCZOS)
        print(image.size, end=" -> ")
        # second resize to make sure the picture as large as possible
        padding_rate = min(width / image.size[0], height / image.size[1])
        image = image.resize((int(padding_rate) * image.size[0], int(padding_rate) * image.size[1]))
        print(image.size)
        new_image.paste(image, (
            w_margin + (idp % 2) * width,
            h_margin + (idp // 2) * height,
            w_margin + (idp % 2) * width + image.size[0],
            h_margin + (idp // 2) * height + image.size[1]
            )
        )
    return new_image

