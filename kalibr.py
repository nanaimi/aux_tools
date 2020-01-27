import numpy as np
import tf

# camera frame name
cam_frame_name = "rgb_cam"
body_frame_name = "dragonfly"

# extrinsics matrix from kalibr
kalibr_matrix=np.array([[0.016869929271473516, -0.9997223078104143, 0.016453350801442057, 0.026392308932125172], \
			[0.0697636321194719, -0.015238671997557629, -0.9974471507349401, 0.01828246767810459], \
			[0.9974208946677802, 0.017974708397375583, 0.06948718398492515, -0.12627449301843877], \
			[0.0, 0.0, 0.0, 1.0]])

kalibr_matrix_inv = np.linalg.inv(kalibr_matrix)

# get quaternion as text
tf_q = tf.transformations.quaternion_from_matrix(kalibr_matrix_inv[0:4,0:4])
tf_q_string = "{:.6f} {:.6f} {:.6f} {:.6f}".format(tf_q[0], tf_q[1], tf_q[2], tf_q[3])

# get position as text
tf_p = kalibr_matrix_inv[0:3,3]
tf_p_string = "{:.4f} {:.4f} {:.4f}".format(tf_p[0], tf_p[1], tf_p[2])

# write static tf publisher
tf_publisher_string = """<node pkg="tf2_ros" type="static_transform_publisher" name="broadcaster_{body}_to_{cam}" args="{pos_string} {quat_string} {body} {cam}" />"""

print(tf_publisher_string.format(cam = cam_frame_name, body = body_frame_name, quat_string = tf_q_string, pos_string = tf_p_string))
