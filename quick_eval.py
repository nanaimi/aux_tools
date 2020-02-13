import rosbag
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import math
import rosbag_pandas
import os
import shutil

set_of_bags = 'fifth_trial'

def create_timecolumn(df, topic, delta=0.0):
    df['time'] = pd.to_datetime(df['{}/header/stamp/secs'.format(topic)], unit='s') + pd.to_timedelta(df['{}/header/stamp/nsecs'.format(topic)], unit='ns') + pd.to_timedelta(delta, unit='s')


### Create directory to save evaluation plots to set
bag_file = "/home/michbaum/datasets/rosbags/ball_position_test_2_2020-02-13-12-36-50.bag"
### End

df_tracker_states = rosbag_pandas.bag_to_dataframe(bag_file, include=['/mbzirc_estimator/imm/state'])
print(df_tracker_states)
# df_tracker_states['time'] = pd.to_datetime(df_tracker_states['/mbzirc_estimator/imm/state/header/stamp/secs'], unit='s') + pd.to_timedelta(df['/mbzirc_estimator/imm/state/header/stamp/nsecs'], unit='ns') + pd.to_timedelta(delta, unit='s')
#
# plt.plot(df_tracker_states['time'], df_tracker_states['/mbzirc_estimator/imm/state/pose/pose/position/x'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
# plt.plot(df_tracker_states['time'], df_tracker_states['/mbzirc_estimator/imm/state/pose/pose/position/y'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
# plt.plot(df_tracker_states['time'], df_tracker_states['/mbzirc_estimator/imm/state/pose/pose/position/z'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
