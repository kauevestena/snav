import rospy
import message_filters
from sensor_msgs.msg import Image, CameraInfo

# def callback(image, camera_info):
#   # Solve all of perception here...

rospy.init_node('republisher',anonymous=False)

image_sub = message_filters.Subscriber('/raspicam_node/image_mono', Image)
info_sub = message_filters.Subscriber('/raspicam_node/camera_info', CameraInfo)

ts = message_filters.TimeSynchronizer([image_sub, info_sub], 30)
# ts.registerCallback(callback)
rospy.spin()