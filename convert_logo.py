import cv2
import numpy as np

img_path = r"c:\Users\GamingX\Desktop\JHF ITT\JHF Logo.jpg"
svg_path = r"c:\Users\GamingX\Desktop\JHF ITT\JHF_Logo.svg"

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Threshold to separate logo and background
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

h, w = img.shape
path_d = ""

for cnt in contours:
    # Slightly smooth the contour
    epsilon = 0.0005 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    for i, pt in enumerate(approx):
        x, y = pt[0]
        # Round to 1 decimal place to save SVG size
        x, y = round(x, 1), round(y, 1)
        if i == 0:
            path_d += f"M{x},{y} "
        else:
            path_d += f"L{x},{y} "
    path_d += "Z "

# SVG string (using fill="currentColor" for perfect adaptability)
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
    <path d="{path_d.strip()}" fill="currentColor" fill-rule="evenodd"/>
</svg>'''

with open(svg_path, "w") as f:
    f.write(svg_content)

print(f"Successfully generated {svg_path}")
