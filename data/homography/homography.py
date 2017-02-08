import cv2
import numpy as np

def homography (file, points, dest):
    # Read source image.
    im_src = cv2.imread(file)
    # Four corners of the book in source image
    p1,p2,p3,p4 = points
    pts_src = np.array([p1, p2, p3, p4], dtype=float)

    # Read destination image.
    im_dst = cv2.imread('result.jpg')
    # Four corners of the book in destination image.
    d1, d2, d3, d4 = dest
    pts_dst = np.array([d1, d2, d3, d4], dtype=float)

    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)

    cv2.waitKey(0)