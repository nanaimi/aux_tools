
import rosbag
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import math
import rosbag_pandas

### some useful functions
def get_columns(df, ):
    cols = []
    for col in df_tracker_states.columns:
        cols.append(col)
    return cols

bag_path = '/home/nasib/datasets/rosbags/evaluation_sets/'
file = 'evaluation_straight_line_2020-01-27-09-30-37.bag'

file_path = bag_path + file

bag_path = '/home/nasib/datasets/rosbags/evaluation_sets/'
file = 'evaluation_straight_line_2020-01-27-09-30-37.bag'

file_path = bag_path + file
df_tracker_states = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/state'])
# Load entire ROSbag into a DataFrame
df = rosbag_pandas.bag_to_dataframe(file_path)

df_tracker_states['time'] = pd.to_datetime(df_tracker_states['/mbzirc_estimator/imm/state/header/stamp/secs'], unit='s') + pd.to_timedelta(df_tracker_states['/mbzirc_estimator/imm/state/header/stamp/nsecs'], unit='ns')

df_tracker_states.plot(x='time', y='/mbzirc_estimator/imm/state/pose/pose/position/x')

# # Load entire ROSbag into a DataFrame
# df = rosbag_pandas.bag_to_dataframe(file_path)
#
# # Load topics of interest into separate DataFrames
# df_tracker_states = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/state'])
# df_tracker_future = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/future'])
# df_tracker_evaluation = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/evaluation'])
# df_groundtruth_ball = rosbag_pandas.bag_to_dataframe(file_path, include=['/rod_with_ball/vrpn_client/estimated_odometry'])
# df_target_world = rosbag_pandas.bag_to_dataframe(file_path, include=['/detection/target_world'])

# state_drop = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83]
# ### list all different columns
# df_tracker_states.drop(df_tracker_states.columns[state_drop], axis=1, inplace=True)
#
#
# ### Index of every row is date and time in ascending order (oldest at the top, newest at the bottom)
# # List of all indices
# l = list(df_top.index.tolist())
#
# t = l[0].time()
# t.day
# t.hour
# t.minute
# t.second
# t.microsecond

d = {'one': np.random.rand(10),
     'two': np.random.rand(10),
     'three': np.random.rand(10)}

df = pd.DataFrame(d)

fig, ax = plt.subplots(nrows=3, ncols=3)
fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95,
                    top=0.9, wspace=0.25, hspace=0.25)

# Tracker states, detection positions, groundtruth
ax[0, 0].plot(df.index, df['one'], 'rx', label='Tracker')           #/mbzirc_estimator/imm/state/pose/pose/position/x
ax[0, 0].plot(df.index, df['two'], 'b^', label='Detection')         #/detection/target_world
ax[0, 0].plot(df.index, df['three'], 'go', label='Groundtruth')     #/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/x
ax[0, 0].set_title("x-coordinate")
ax[0, 0].legend(loc="upper right")

ax[0, 1].plot(df.index, df['one'], 'rx', label='Tracker')           #/mbzirc_estimator/imm/state/pose/pose/position/y
ax[0, 1].plot(df.index, df['two'], 'b^', label='Detection')         #/detection/target_world
ax[0, 1].plot(df.index, df['three'], 'go', label='Groundtruth')     #/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/y
ax[0, 1].set_title("y-coordinate")
ax[0, 1].legend(loc="upper right")

ax[0, 2].plot(df.index, df['one'], 'rx', label='Tracker')           #/mbzirc_estimator/imm/state/pose/pose/position/z
ax[0, 2].plot(df.index, df['two'], 'b^', label='Detection')         #/detection/target_world
ax[0, 2].plot(df.index, df['three'], 'go', label='Groundtruth')     #/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/z
ax[0, 2].set_title("z-coordinate")
ax[0, 2].legend(loc="upper right")

# NOTE: correct timestamp of future poses by adding the time delta --> 0.2 sec?
### future positions and actual positions
color = 'tab:red'
ax[1, 0].plot(df.index, df['one'], 'rx', label='Future')            #/mbzirc_estimator/imm/state/pose/pose/position/x
ax[1, 0].plot(df.index, df['two'], 'b^', label='Detections')        #/detection/target_world/pose/pose/position/x
ax[1, 0].plot(df.index, df['three'], 'go', label='Groundtruth')     #/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/x
ax[1, 0].set_title("x-coordinate")
ax[1, 0].legend(loc="upper right")
ax[1, 0].tick_params(axis='y', labelcolor=color)

ax[1, 1].plot(df.index, df['one'], 'rx', label='Future')            #/mbzirc_estimator/imm/state/pose/pose/position/y
ax[1, 1].plot(df.index, df['two'], 'b^', label='Detections')        #/detection/target_world/pose/pose/position/y
ax[1, 1].plot(df.index, df['three'], 'go', label='Groundtruth')     #/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/y
ax[1, 1].set_title("y-coordinate")
ax[1, 1].legend(loc="upper right")
ax[1, 1].tick_params(axis='y', labelcolor=color)

ax[1, 2].plot(df.index, df['one'], 'rx', label='Future')            #/mbzirc_estimator/imm/state/pose/pose/position/z
ax[1, 2].plot(df.index, df['two'], 'b^', label='Detections')        #/detection/target_world/pose/pose/position/z
ax[1, 2].plot(df.index, df['three'], 'go', label='Groundtruth')     #/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/z
ax[1, 2].set_title("z-coordinate")
ax[1, 2].legend(loc="upper right")
ax[1, 2].tick_params(axis='y', labelcolor=color)

# Second Axis for covariance
color = 'tab:blue'
ax2 = [None] * 4
ax2[0] = ax[1, 0].twinx()
ax2[0].set_ylabel('var', color=color)
ax2[0].plot(df.index, df['one'], color=color)                       # Variance of future for x direction
ax2[0].tick_params(axis='y', labelcolor=color)

ax2[1] = ax[1, 1].twinx()
ax2[1].set_ylabel('var', color=color)
ax2[1].plot(df.index, df['one'], color=color)                       # Variance of future for y direction
ax2[1].tick_params(axis='y', labelcolor=color)

ax2[2] = ax[1, 2].twinx()
ax2[2].set_ylabel('var', color=color)
ax2[2].plot(df.index, df['one'], color=color)                       # Variance of future for z direction
ax2[2].tick_params(axis='y', labelcolor=color)


# Plots for evaluation message plotting
ax[2, 0].plot(df.index, df['one'], 'rx', label='Error')
ax[2, 0].set_title("Estimator Error and RMSE")
ax[2, 0].legend(loc="upper right")

ax[2, 1].plot(df.index, df['one'], 'rx', label='Error')
ax[2, 1].set_title("Measurement Error and RMSE")
ax[2, 1].legend(loc="upper right")

color = 'tab:blue'
ax3 = [None] * 3
ax3[0] = ax[2, 0].twinx()
ax3[0].set_ylabel('RMSE', color=color)
ax3[0].plot(df.index, df['one'], color=color)                       # Estimator RMSE
ax3[0].tick_params(axis='y', labelcolor=color)

ax3[0] = ax[2, 1].twinx()
ax3[0].set_ylabel('RMSE', color=color)
ax3[0].plot(df.index, df['one'], color=color)                       # Measurement RMSE
ax3[0].tick_params(axis='y', labelcolor=color)

# for i in list_of_model_probabilities:
#     ax[2, 2].plot(df.index, df[i.model_name], label='Model {} Likelihood'.format(i.model_name))

# ax[2, 2].plot(df.index, df['one'], 'rx', label='Model 1 Likelihood')
# ax[2, 2].plot(df.index, df['two'], 'b^', label='Model 2 Likelihood')
# ax[2, 2].plot(df.index, df['two'], 'b^', label='Model 3 Likelihood')
# ax[2, 2].plot(df.index, df['two'], 'b^', label='Model 4 Likelihood')
# ax[2, 2].plot(df.index, df['two'], 'b^', label='Model 5 Likelihood')
# ax[2, 2].plot(df.index, df['two'], 'b^', label='Model 6 Likelihood')
ax[2, 2].set_title("Model Likelihoods")
ax[2, 2].legend(loc="upper right")


plt.show()


# Graph Outline
#################################################################################
#                                                                               #
#                                                                               #
#                                                                               #
#              Graph with Tracker state, groundtruth states, and the            #
#                     direct measurements in the world frame                    #
#                                                                               #
#                                                                               #
#                                                                               #
#################################################################################
#                                                                               #
#                                                                               #
#                                                                               #
#      Future states plotted versus the actual states at the future times       #
#                   Plot model covariance of future as well                     #
#                                                                               #
#                                                                               #
#                                                                               #
#################################################################################
#                 #                                      #                      #
#                 #                                      #                      #
#                 #                                      #                      #
#                 #         Plot evaluation msg          #                      #
#                 #                                      #                      #
#                 #                                      #                      #
#                 #                                      #                      #
#################################################################################
