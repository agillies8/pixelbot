import pixellib
from pixellib.semantic import semantic_segmentation
import cv2

#experimental script to play with better pixelators using various CV techniques. Sort of a mess right now

segment_frame = semantic_segmentation()
segment_frame.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5") 
#segment_image.segmentAsPascalvoc("../images/person.jpg", output_image_name = "../images/image_new.jpg")


vid = cv2.VideoCapture(0) 

while(True):

    # Input image
    #input = cv2.imread('../images/person.jpg')

    ret, input = vid.read() 
    
    #input = cv2.imread('../images/person.jpg')
    segmap, output = segment_frame.segmentFrameAsPascalvoc(input)

    cv2.imshow('Input', input)
    cv2.imshow('Output', output)

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 