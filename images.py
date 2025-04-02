import cv2
import numpy as np

def sketch_to_image(sketch_path, output_path):
    sketch_image = cv2.imread(sketch_path, cv2.IMREAD_GRAYSCALE)
    inverted_sketch = cv2.bitwise_not(sketch_image)
    blurred_image = cv2.GaussianBlur(inverted_sketch, (21, 21), 0)
    result_image = cv2.bitwise_not(blurred_image)
    cv2.imwrite(output_path, result_image)
input_sketch_path = r'C:\Users\Meduri Bhagavan\Pictures\Saved Pictures\hima3.jpg'  # Path to your pencil sketch image
output_image_path = 'restored_image.jpg'  
sketch_to_image(input_sketch_path, output_image_path)
