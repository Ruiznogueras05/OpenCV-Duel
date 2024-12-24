import cv2
import numpy as np

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Create the background subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Loop indefinitely
while True:
    # Capture the current frame
    _, frame = cap.read()

    # Apply the background subtractor to the frame
    mask = bg_subtractor.apply(frame)

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of red colors in the HSV color space
    lower_red = (0, 50, 50)
    upper_red = (10, 255, 255)

    # Create a mask for only the red colors
    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    # Invert the mask to get the background
    bg_mask = cv2.bitwise_not(mask)

    # Combine the red mask and the inverted mask to get the red background
    red_bg_mask = cv2.bitwise_and(red_mask, bg_mask)

    # Use the red background mask to create a red background image
    red_bg = np.zeros_like(frame, dtype=np.uint8)
    red_bg[:,:,2] = red_bg_mask

    # Show the frame with the red background
    cv2.imshow("Frame", frame)
    cv2.imshow("Red Background", red_bg)

    # Check for the Esc key being pressed, and if so, stop the loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
