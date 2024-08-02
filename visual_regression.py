from random import randint
import pathlib

from PIL import Image, ImageChops
from pixelmatch.contrib.PIL import pixelmatch


def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return width * height


def vr(img1, img2, per_diff=0.1, pix_diff=100):

    filename_path_1 = pathlib.Path(img1)
    filename_path_2 = pathlib.Path(img2)

    print("Comparing", filename_path_1, "vs", filename_path_2)
    with Image.open(filename_path_1) as im1:
        with Image.open(filename_path_2) as im2:
            max_size = (max(im1.width, im2.width), max(im1.height, im2.height))
            imA = Image.new("RGB", max_size)
            imA.paste(im1.convert("RGB"))
            imB = Image.new("RGB", max_size)
            imB.paste(im2.convert("RGB"))
    translucent = Image.new("RGB", imA.size, (255, 0, 0))
    mask = ImageChops.difference(imA, imB).convert("L").point(lambda x: 127 if x else 0)
    imB.paste(translucent, (0, 0), mask)
    print("Done")
    imB.save(f"./diff__pil_{img1}__v__{img2}_{randint(1000, 9999)}.png")
    img_a = Image.open(filename_path_1)
    img_b = Image.open(filename_path_2)
    img_diff = Image.new("RGBA", img_a.size)

    # note how there is no need to specify dimensions
    mismatch = pixelmatch(img_a, img_b, img_diff, threshold=0.1, includeAA=True)
    num_pixels = int(get_num_pixels(filename_path_1))
    percentage_diff = (mismatch / num_pixels) * 100
    print(
        f"num_mismatch_pixels: {mismatch} total_num_pixels: {num_pixels} \npercentage difference: {percentage_diff:.2f}%"
    )  # mismatch, num_pixels, (mismatch / num_pixels) * 100)
    # small dot gives = 193
    # identical has mismatch = 6867
    if num_pixels > pix_diff:
        print(f"❌ Images not pixel equal: {num_pixels}px difference")
    if percentage_diff > per_diff:
        print(f"❌ Images not percent equal: {round(percentage_diff,2)}% difference")

    img_diff.save(f"./diff_pixelmatch_{img1}__v__{img2}_{randint(1000, 9999)}.png")


if __name__ == "__main__":
    vr("screenshot-1.jpg", "screenshot-2.jpg")
