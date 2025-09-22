
import cv2
import numpy as np
    # Create a black image
    img = np.zeros((500, 500, 3), np.uint8)
    # Draw a red line from (50,50) to (450,450) with thickness 5
    cv2.line(img, (50, 50), (450, 450), (0, 0, 255), 5)

    # Display the image
    cv2.imshow("Image with Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()