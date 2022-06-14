# Learned from the YouTube channel: Murtaza's Workshop

# import cv2
# import pytesseract

# # For reading an image
# img = cv2.imread('imageD.png')
# # For converting color of the image from BGR to RGB (BGR is default in OpenCV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # Getting the shape of the image
# hImg, wImg, _ = img.shape

################################
### Detecting Each Character ###
################################

# # Configuration value for getting only the digits. Add this as the argument to the config parameter of image_to_boxes
# conf = r'--oem 3 --psm 6 outputbase digits'

# # List out the content and box coordinates of the characters
# boxes = pytesseract.image_to_boxes(img)

# # Convert each line to a string which is an item of the whole list
# boxes = boxes.splitlines()

# for box in boxes:
#     # Create a list for each characters' details
#     box = box.split(' ')
#     # Conversion to integer
#     x1, y1, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])

#     # Create a rectangle around the characters
#     cv2.rectangle(img, (x1, hImg-y1), (x2, hImg-y2), (0, 0, 255), 3)
#     # Create a text for each character
#     cv2.putText(img, box[0], (x1, hImg-y1+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

# # Show the image in a window with specifying the name
# cv2.imshow('Result', img) 
# # Wait infinitely until a key is pressed
# cv2.waitKey(0)   


################################
###      Detecting Words     ###
################################

# # Detect whole words 
# data = pytesseract.image_to_data(img)

# data = data.splitlines()

# # get the id in addition to the items
# for line_index, data_item in enumerate(data):
#     # skip the heading line
#     if line_index != 0:
#         data_item = data_item.split()
#         # take only needed items containing our data
#         if len(data_item) == 12:
#             x1, y1, x2, y2 = int(data_item[6]), int(data_item[7]), int(data_item[8]), int(data_item[9])
#             cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (0, 0, 255), 3)
#             cv2.putText(img, data_item[11], (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

# # Show the image in a window with specifying the name
# cv2.imshow('Result', img) 
# # Wait infinitely until a key is pressed
# cv2.waitKey(0) 


