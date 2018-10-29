import numpy as np
import cv2

def DrawText(img,left_R, right_R,bottom_lane_position):

    xm_per_pix = 3.7 / 700

    lane_mid = np.average(bottom_lane_position)*xm_per_pix

    # print("The output from draw is ",left_R,right_R)
    # if left_R > right_R:
    #     car_R = -np.average([left_R,right_R])
    # else:
    #     car_R = np.average([left_R,right_R])

    car_R = np.average([left_R,right_R])
    print(left_R,right_R)

    car_pos = img.shape[1]/2*xm_per_pix
    car_offset = car_pos-lane_mid

    # if car_R < 0:
    #     direction_r = 'Right'
    # else:
    #     direction_r = 'Left'

    if abs(car_R)>2500:
        text1 = 'The lane is straight'
    else:
        text1 = 'Curve Radius : '+'{:04.2f}'.format(abs(car_R))+' m'
    cv2.putText(img,text1,(40,70),cv2.FONT_HERSHEY_DUPLEX,1.5,(200,255,255),2,cv2.LINE_AA)
    if car_offset>0:
        direction_p = 'Right'
    else:
        direction_p = 'Left'

    text2 = '{:04.2f}'.format(abs(car_offset))+' m '+direction_p+' of center'

    cv2.putText(img,text2,(40,120),cv2.FONT_HERSHEY_DUPLEX,1.5,(200,255,255),2,cv2.LINE_AA)

    return img
