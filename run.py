import os
import time
import json
from utils.printer import *
from utils.util_image import *


def get_pic(path, step):
    pictures = os.listdir(path)
    for pics in range(0, len(pictures), step):
        if pics == 0:
            last = pics
            continue
        yield pictures[last: pics]
        last = pics
    if len(pictures) > last:
        yield pictures[last:]


def read_config(path="config.json"):
    with open(path, encoding="utf-8") as f:
        return json.loads(f.read())


def main():
    path = "./buffer"
    if not os.path.exists("output"):
        os.mkdir("output")

    start_time = time.strftime("%Y%m%d%H%M%S")
    if not os.path.exists(start_time):
        os.mkdir("output/" + start_time)

    print("Starting...")
    config = read_config()
    for ind, pics in enumerate(get_pic(path=path, step=4)):
        print("PIC:", ind + 1)
        print(50 * "-")
        print("original image size:")
        new_img = reg_pic(pics, path=path, config=config)
        print("output image size:")
        print(new_img.size)
        print("rate: " + str(new_img.size[0] / new_img.size[1]))
        now_time = time.strftime("%Y%m%d%H%M%S")
        new_img.save("./output/{}/{}-{}.jpg".format(start_time, now_time, str(ind)))
        print("picture saved: ./output/{}/{}-{}.jpg".format(start_time, now_time, str(ind+1)))
        print()
        printer(new_img)
    print("Done")


if __name__ == "__main__":
    main()
