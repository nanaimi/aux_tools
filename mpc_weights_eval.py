import rosbag
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import math
import rosbag_pandas
import os
import shutil

### Parameters that must be set before running script

set_of_bags = 'fifth_trial'

### some useful functions
def get_columns(df):
    cols = []
    for col in df.columns:
        print(col)
        cols.append(col)
    return cols

def create_timecolumn(df, topic, delta=0.0):
    df['time'] = pd.to_datetime(df['{}/header/stamp/secs'.format(topic)], unit='s') + pd.to_timedelta(df['{}/header/stamp/nsecs'.format(topic)], unit='ns') + pd.to_timedelta(delta, unit='s')

def time_rectifier():
    pass

def strip_name(str):
    newstr = ''
    index = str.index('.')
    newstr = str[:index]
    newstr = 'plots_' + newstr
    return newstr

def filter_list_of_files(list):
    list_to_remove = []
    for file in list:
        if file.endswith(".txt"):
            list_to_remove.append(file)
    for rem in list_to_remove:
        list.remove(rem)

def copy_settings_files_to_plot_directory(list, src_directory_path, plot_directory_path):
    for file in list:
        if file.endswith(".txt"):
            print('copying {}'.format(file))
            shutil.copy2(src_directory_path + '/' + file, plot_directory_path)
            print('finished copying {}'.format(file))

### End of function definitions

### Create directory to save evaluation plots to set
parent_dir = "/home/nasib/datasets/evaluated"
path_plots = os.path.join(parent_dir, set_of_bags)
os.mkdir(path_plots)
### End

### Specify path to directory containing rosbags for evaluation
bag_path = "/home/nasib/datasets/rosbags/evaluation_sets/" + set_of_bags
files_list = os.listdir(bag_path)
print(files_list)

file_path = bag_path + '/' + file
plot_file = strip_name(file)

### Load all different topics into separate DataFrames
df_mpc_weights = rosbag_pandas.bag_to_dataframe(file_path, include=['/peregrine/mpc_costs'])

### Create time column for every DataFrame
create_timecolumn(df_mpc_weights, '/peregrine/mpc_costs')

### Plot all relevant information
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots(nrows=3, ncols=1)
fig.suptitle(plot_file)
fig.set_size_inches(h=14, w=21)
fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95,
                    top=0.9, wspace=0.25, hspace=0.25)

# Tracker states, detection positions, groundtruth
ax[0].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/0'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='')
ax[0].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/1'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detection')
ax[0].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/2'],color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
ax[0].set_title("x-coordinate")
ax[0].legend(loc="upper right")

ax[1].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/3'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
ax[1].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/4'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detection')
ax[1].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/5'],color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
ax[1].set_title("y-coordinate")
ax[1].legend(loc="upper right")

ax[2].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/6'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
ax[2].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/7'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detection')
ax[2].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/8'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
ax[2].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/9'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
ax[2].plot(df_mpc_weights['time'], df_mpc_weights['/peregrine/mpc_costs/pose/covariance/10'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
ax[2].set_title("z-coordinate")
ax[2].legend(loc="upper right")


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
