import rosbag
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import math
import rosbag_pandas
import os

directory = "params____"

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
    str.index('.')
    newstr = str[:index]
    newstr = 'plots_' + newstr
    return newstr

### Specify bag folder path and file name

# Parent Directory path
parent_dir = "/home/nasib/datasets/evaluated"

# Path to plots
path_plots = os.path.join(parent_dir, directory)

os.mkdir(path)

bag_path = '/home/nasib/datasets/rosbags/evaluation_sets/'
files_list = os.listdir(bag_path)

file = 'evaluation_straight_line_2020-01-27-09-30-37.bag'
for file in files_list:

    file_path = bag_path + file
    plot_file = strip_name(file)
    ### Load all different topics into separate DataFrames
    df_tracker_states = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/state'])
    df_tracker_future = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/future'])
    df_tracker_evaluation = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/evaluation'])
    df_groundtruth_ball = rosbag_pandas.bag_to_dataframe(file_path, include=['/rod_with_ball/vrpn_client/estimated_odometry'])
    df_target_world = rosbag_pandas.bag_to_dataframe(file_path, include=['/detection/target_world'])

    # Load entire ROSbag into a DataFrame
    df = rosbag_pandas.bag_to_dataframe(file_path)

    ### Create time column for every DataFrame
    create_timecolumn(df_tracker_states, '/mbzirc_estimator/imm/state')
    create_timecolumn(df_tracker_future, '/mbzirc_estimator/imm/future')
    create_timecolumn(df_tracker_evaluation, '/mbzirc_estimator/imm/evaluation')
    create_timecolumn(df_groundtruth_ball, '/rod_with_ball/vrpn_client/estimated_odometry')
    create_timecolumn(df_target_world, '/detection/target_world')


    ### Plot all relevant information
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots(nrows=3, ncols=3)
    fig.suptitle('Linear motion, Parameters: ')
    fig.set_size_inches(h=14, w=21)
    fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95,
                        top=0.9, wspace=0.25, hspace=0.25)

    # Tracker states, detection positions, groundtruth
    ax[0, 0].plot(df_tracker_states['time'], df_tracker_states['/mbzirc_estimator/imm/state/pose/pose/position/x'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
    ax[0, 0].plot(df_target_world['time'], df_target_world['/detection/target_world/pose/pose/position/x'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detection')
    ax[0, 0].plot(df_groundtruth_ball['time'], df_groundtruth_ball['/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/x'],color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
    ax[0, 0].set_title("x-coordinate")
    ax[0, 0].legend(loc="upper right")

    ax[0, 1].plot(df_tracker_states['time'], df_tracker_states['/mbzirc_estimator/imm/state/pose/pose/position/y'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
    ax[0, 1].plot(df_target_world['time'], df_target_world['/detection/target_world/pose/pose/position/y'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detection')
    ax[0, 1].plot(df_groundtruth_ball['time'], df_groundtruth_ball['/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/y'],color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
    ax[0, 1].set_title("y-coordinate")
    ax[0, 1].legend(loc="upper right")

    ax[0, 2].plot(df_tracker_states['time'], df_tracker_states['/mbzirc_estimator/imm/state/pose/pose/position/z'], color='darkblue', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Tracker')
    ax[0, 2].plot(df_target_world['time'], df_target_world['/detection/target_world/pose/pose/position/z'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detection')
    ax[0, 2].plot(df_groundtruth_ball['time'], df_groundtruth_ball['/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/z'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
    ax[0, 2].set_title("z-coordinate")
    ax[0, 2].legend(loc="upper right")

    # NOTE: correct timestamp of future poses by adding the time delta --> 0.2 sec?
    ### future positions and actual positions
    color = 'tab:red'
    ax[1, 0].plot(df_tracker_future['time'], df_tracker_future['/mbzirc_estimator/imm/future/pose/pose/position/x'], color='orchid', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Future')
    ax[1, 0].plot(df_target_world['time'], df_target_world['/detection/target_world/pose/pose/position/x'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detections')
    ax[1, 0].plot(df_groundtruth_ball['time'], df_groundtruth_ball['/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/x'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
    ax[1, 0].set_title("x-coordinate")
    ax[1, 0].legend(loc="upper right")
    ax[1, 0].tick_params(axis='y', labelcolor=color)

    ax[1, 1].plot(df_tracker_future['time'], df_tracker_future['/mbzirc_estimator/imm/future/pose/pose/position/y'], color='orchid', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Future')
    ax[1, 1].plot(df_target_world['time'], df_target_world['/detection/target_world/pose/pose/position/y'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detections')
    ax[1, 1].plot(df_groundtruth_ball['time'], df_groundtruth_ball['/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/y'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
    ax[1, 1].set_title("x-coordinate")
    ax[1, 1].legend(loc="upper right")
    ax[1, 1].tick_params(axis='y', labelcolor=color)

    ax[1, 2].plot(df_tracker_future['time'], df_tracker_future['/mbzirc_estimator/imm/future/pose/pose/position/z'], color='orchid', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Future')
    ax[1, 2].plot(df_target_world['time'], df_target_world['/detection/target_world/pose/pose/position/z'], color='green', marker='^', linestyle='dotted', linewidth=1, markersize=3, label='Detections')
    ax[1, 2].plot(df_groundtruth_ball['time'], df_groundtruth_ball['/rod_with_ball/vrpn_client/estimated_odometry/pose/pose/position/z'], color='red', marker='o', linestyle='dotted', linewidth=1, markersize=3, label='Groundtruth')
    ax[1, 2].set_title("x-coordinate")
    ax[1, 2].legend(loc="upper right")
    ax[1, 2].tick_params(axis='y', labelcolor=color)

    # Second Axis for covariance
    color = 'tab:blue'
    ax2 = [None] * 4
    ax2[0] = ax[1, 0].twinx()
    ax2[0].set_ylabel('var', color=color)
    ax2[0].plot(df_tracker_future['time'], df_tracker_future['/mbzirc_estimator/imm/future/pose/covariance/0'], color=color)
    ax2[0].tick_params(axis='y', labelcolor=color)

    ax2[1] = ax[1, 1].twinx()
    ax2[1].set_ylabel('var', color=color)
    ax2[1].plot(df_tracker_future['time'], df_tracker_future['/mbzirc_estimator/imm/future/pose/covariance/7'], color=color)                       # Variance of future for y direction
    ax2[1].tick_params(axis='y', labelcolor=color)

    ax2[2] = ax[1, 2].twinx()
    ax2[2].set_ylabel('var', color=color)
    ax2[2].plot(df_tracker_future['time'], df_tracker_future['/mbzirc_estimator/imm/future/pose/covariance/14'], color=color)                       # Variance of future for z direction
    ax2[2].tick_params(axis='y', labelcolor=color)

    ### Plots for evaluation message plotting
    color = 'tab:red'
    ax[2, 0].plot(df_tracker_evaluation['time'], df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/estimator_error'], color=color, label='Error')
    ax[2, 0].set_title("Estimator Error and RMSE")
    ax[2, 0].tick_params(axis='y', labelcolor=color)
    ax[2, 0].set_ylabel('Error', color=color)
    ax[2, 0].set_ylim([0,13])

    ax[2, 1].plot(df_tracker_evaluation['time'], df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/measurement_error'], color=color, label='Error')
    ax[2, 1].set_title("Measurement Error and RMSE")
    ax[2, 1].tick_params(axis='y', labelcolor=color)
    ax[2, 1].set_ylabel('Error', color=color)
    ax[2, 1].set_ylim([0,13])

    color = 'tab:blue'
    ax3 = [None] * 3
    ax3[0] = ax[2, 0].twinx()
    ax3[0].set_ylabel('RMSE', color=color)
    ax3[0].plot(df_tracker_evaluation['time'], df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/estimator_rmse'], color=color, label='RMSE')                       # Estimator RMSE
    ax3[0].tick_params(axis='y', labelcolor=color)
    ax3[0].set_ylim([0,2])

    ax3[1] = ax[2, 1].twinx()
    ax3[1].set_ylabel('RMSE', color=color)
    ax3[1].plot(df_tracker_evaluation['time'], df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/measurement_rmse'], color=color, label='RMSE')                       # Estimator RMSE
    ax3[1].tick_params(axis='y', labelcolor=color)
    ax3[1].set_ylim([0,2])

    for i in range(8):
        ax[2, 2].plot(df_tracker_evaluation['time'], df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/model_probabilities/{}/probability'.format(i)], label='Model {} Likelihood'.format(df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/model_probabilities/{}/model_name'.format(i)].iloc[0]))

    ax[2, 2].tick_params(axis='y', labelcolor='black')
    ax[2, 2].set_ylabel('Probability', color='black')
    ax[2, 2].legend(loc="upper right")

    ax4 = ax[2, 2].twinx()
    ax4.plot(df_tracker_evaluation['time'], df_tracker_evaluation['/mbzirc_estimator/imm/evaluation/cov_norm'], color='black')
    ax4.tick_params(axis='y', labelcolor='black')
    ax4.set_ylabel('Covariance Norm', color='black')
    plt.show()
    fig.savefig(os.path.join(path_plots, plot_file))


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
