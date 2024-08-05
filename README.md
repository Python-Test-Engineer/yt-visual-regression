# Visual Regression


## Links

https://github.com/whtsky/pixelmatch-py

https://pypi.org/project/pixelmatch/

https://playwright.dev/python/docs/screenshots

## YouTube

## Cookbook

[https://pytest-cookbook.com/toolbox/visual_regression/](https://pytest-cookbook.com/toolbox/visual_regression/)

## YouTube

[https://www.youtube.com/watch?v=wMjsrsQK3hs](https://www.youtube.com/watch?v=wMjsrsQK3hs)

## Info

Given two images screenshot-1.jpg and screenshot-2.jpg, `visual_regression.py` will produce two images:

- `diff__pil_screenshot-1.jpg__v__screenshot-2.jpg_1288.png` shows highlights difference.
- `diff_pixelmatch_screenshot-1.jpg__v__screenshot-2.jpg_7152.png` is an image just of the difference.

NB a random int is added at end of filename to avoid over-writing files.

`visual_regrssion.py` is customisable and outputs the following:

![output](./_images/output.png)
