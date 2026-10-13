import cv2, math
import numpy as np

indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for INDEX in indexes:
    img = cv2.imread(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/coin_demo{INDEX}.png")
    gray = cv2.imread(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/coin_demo{INDEX}.png", cv2.IMREAD_GRAYSCALE)


    if img is None or gray is None:
        raise FileNotFoundError

    chosen = img.copy()
    draw = chosen.copy()
    print("img", img.shape, img.dtype)
    print("gray", gray.shape, gray.dtype)

    bg = chosen[10:60, 10:60]
    edge = chosen[120, 50:66]

    # print('bg', bg.min(), bg.max(), bg.std())
    # print('edge', edge.tolist())
    gauss = cv2.GaussianBlur(chosen, (5, 5), 0)
    # print('bg', gauss[10:60, 10:60].min(), gauss[10:60, 10:60].max(), gauss[10:60, 10:60].std())
    # print('edge', gauss[120, 50:66].tolist())
    med = cv2.medianBlur(chosen, 5)
    # print('bg', med[10:60, 10:60].min(), med[10:60, 10:60].max(), med[10:60, 10:60].std())
    # print('edge', med[120, 50:66].tolist())
    blur = cv2.blur(chosen, (5, 5))
    # print('bg', blur[10:60, 10:60].min(), blur[10:60, 10:60].max(), blur[10:60, 10:60].std())
    # print('edge', blur[120, 50:66].tolist())
    bilateral = cv2.bilateralFilter(chosen, 5, 10, 10)
    # print('bg', bilateral[10:60, 10:60].min(), bilateral[10:60, 10:60].max(), bilateral[10:60, 10:60].std())
    # print('edge', bilateral[120, 50:66].tolist())

    blurred = cv2.cvtColor(med, cv2.COLOR_BGR2GRAY)

    inrange = cv2.inRange(blurred, 62, 205)
    threshold = cv2.threshold(blurred, 205, 255, cv2.THRESH_BINARY_INV)[1]

    masked = inrange

    morph_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morph_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    morph_diamond = cv2.getStructuringElement(cv2.MORPH_DIAMOND, (5, 5))
    morphed = cv2.morphologyEx(masked, cv2.MORPH_OPEN, morph_ellipse)

    contours, hierarchy = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(morphed, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    print(len(contours))


    actual_contours = []
    for contour in contours:
        print(len(contour), contour.shape)
        area = cv2.contourArea(contour)
        diameter = cv2.minEnclosingCircle(contour)[1] * 2
        perimeter1 = math.pi * diameter
        perimeter2 = cv2.arcLength(contour, True)
        circularity = (4 * math.pi * area) / (perimeter2 ** 2)
        
        if area > 1000 and circularity > 0.7:
            actual_contours.append(contour)
        
        print(area, diameter, perimeter2, circularity)
        
    sort = sorted(actual_contours, key=lambda n: cv2.contourArea(n))
    max_jump = 0
    lower_val = 0
    for i in range(len(sort) - 1):
        if cv2.contourArea(sort[i + 1]) - cv2.contourArea(sort[i]) > max_jump: 
            max_jump = cv2.contourArea(sort[i + 1]) - cv2.contourArea(sort[i])
            lower_val = cv2.contourArea(sort[i])
            
    for i in range(len(actual_contours)):
        c = actual_contours[i]
        size = 'low' if cv2.contourArea(c) < lower_val + max_jump / 2 else 'high'
        moment = cv2.moments(c)
        color = (0, 0, 255) if size == 'low' else (255, 255, 0)
        cv2.drawContours(draw, actual_contours, i, color, 5)
        if moment['m00']:
            center = (moment["m10"] / moment['m00'], moment['m01'] / moment['m00'])
            center = (round(center[0]), round(center[1]))
            cv2.drawMarker(draw, center, color, cv2.MARKER_CROSS, 20, 4, cv2.LINE_4)
        
        


    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/img{INDEX}.png", img)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/gray{INDEX}.png", gray)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/gauss{INDEX}.png", gauss)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/med{INDEX}.png", med)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/blur{INDEX}.png", blur)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/bilateral{INDEX}.png", bilateral)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/blurred{INDEX}.png", blurred)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/inrange{INDEX}.png", inrange)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/threshold{INDEX}.png", threshold)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/masked{INDEX}.png", masked)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/morphed{INDEX}.png", morphed)
    cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Coin Counter/image {INDEX}/FINAL{INDEX}.png", draw)