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

def create_timecolumn(df, topic, delta=0.0):
    df['time'] = pd.to_datetime(df['{}/header/stamp/secs'.format(topic)], unit='s') + pd.to_timedelta(df_tracker_states['{}/header/stamp/nsecs'.format(topic)], unit='ns') + pd.to_timedelta(delta, unit='s')

bag_path = '/home/nasib/datasets/rosbags/evaluation_sets/'
file = 'evaluation_straight_line_2020-01-27-09-30-37.bag'

file_path = bag_path + file

df_tracker_states = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/state'])
# Load entire ROSbag into a DataFrame
df = rosbag_pandas.bag_to_dataframe(file_path)

create_timecolumn(df_tracker_states, '/mbzirc_estimator/imm/state')


plt.style.use('seaborn-whitegrid')
df_tracker_states.plot(x='time', y='/mbzirc_estimator/imm/state/pose/pose/position/x', color='beige')

df_tracker_states.plot(x='time', y='/mbzirc_estimator/imm/state/pose/pose/position/y')

df_tracker_states.plot(x='time', y='/mbzirc_estimator/imm/state/pose/pose/position/z')
