"""This module scans for wild pokemon discord alert"""
import cv2 as cv

IMG_COLOR = cv.imread('screenshot.png')
IMG_COPY = IMG_COLOR.copy()
IMG = cv.imread('screenshot.png', 0)
TEMPLATE = cv.imread('template.PNG', 0)
W, H = TEMPLATE.shape[::-1]

METHODS = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED',
           'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

METHOD = eval('cv.TM_CCOEFF')

RET_VAL = cv.matchTemplate(IMG, TEMPLATE, METHOD)
MIN_VAL, MAX_VAL, MIN_LOC, MAX_LOC = cv.minMaxLoc(RET_VAL)

TOP_LEFT = MAX_LOC
#BOTTOM_RIGHT = (TOP_LEFT[0] + W, TOP_LEFT[1] + H)

POKEMON_LOC = (TOP_LEFT[0] + 40, TOP_LEFT[1] + 100)

CROP = IMG_COPY[POKEMON_LOC[1]: POKEMON_LOC[1]+300,
                POKEMON_LOC[0]: POKEMON_LOC[0]+270]

#cv.rectangle(IMG, TOP_LEFT, BOTTOM_RIGHT, 255, 2)

cv.imwrite('result.png', CROP)
