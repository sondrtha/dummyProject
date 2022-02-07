"""
Tests in subfolders will not be found and run
"""


import utils

def test_get_cropped_img():   # this unit test requires opencv to be installed, if opencv is install you can uncomment this line
    import cv2
    import os
    dirname = os.path.dirname(__file__)
    file_path = dirname + "//kingsdomino.jpg"
    img = cv2.imread(file_path)
    cropped_img = utils.get_cropped_img(img, 0,0,600,500)
    h,w = cropped_img.shape[:2]
    assert(w == 601)
    assert(h == 500)


def test_multiply_by_three():
    assert(utils.multiply_by_three(5) == 15)
    assert(utils.multiply_by_three(10) == 30)

def test_add5():
    assert(utils.add5(10) == 15)
