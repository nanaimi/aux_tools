import rosbag
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import math

### tutorial for rosbag_pandas
import rosbag_pandas

bag_path = '/home/nasib/datasets/rosbags/evaluation_sets/'
file = 'evaluation_straight_line_2020-01-27-09-30-37.bag'

file_path = bag_path + file
df_tracker_states = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/state'])
# Load entire ROSbag into a DataFrame
df = rosbag_pandas.bag_to_dataframe(file_path)

# # Load topics of interest into separate DataFrames
# # df_exclude = rosbag_pandas.bag_to_dataframe('data/example.bag', exclude=['/scan'])
# df_tracker_states = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/state'])
# df_tracker_future = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/future'])
# df_tracker_evaluation = rosbag_pandas.bag_to_dataframe(file_path, include=['/mbzirc_estimator/imm/evaluation'])
# df_groundtruth_ball = rosbag_pandas.bag_to_dataframe(file_path, include=['/rod_with_ball/vrpn_client/estimated_odometry'])
# df_target_world = rosbag_pandas.bag_to_dataframe(file_path, include=['/detection/target_world'])

columns_to_drop = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83]
### list all different columns
df_tracker_states.drop(df_tracker_states.columns[columns_to_drop], axis=1, inplace=True)

for col in df_tracker_states.columns:
    print(col)

### Index of every row is date and time in ascending order (oldest at the top, newest at the bottom)
# List of all indices
l = list(df_top.index.tolist())

t = l[0].time()
t.day
t.hour
t.minute
t.second
t.microsecond



### Graph Outline
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
#                                                                               #
#                                                                               #
#                                                                               #
#               Plot evaluation msg (Look what it even contains)                #
#                                                                               #
#                                                                               #
#                                                                               #
#################################################################################
#                                                                               #
#                                                                               #
#                                                                               #
#            Plot Model Likelihoods (contained in evaluation message)           #
#                                                                               #
#                                                                               #
#                                                                               #
#################################################################################





# Select a dataframe key based on topic and (conform msgevalgen pattern http://docs.ros.org/api/rostopic/html/)
# print(df['/rosout/header/stamp/secs'].to_string())
print(df_include)
print(df.dtypes)

# Obtain possible ROS topics from a selection pattern (conform msgevalgen pattern http://docs.ros.org/api/rostopic/html/)
# This will return the possible topics: /pose, /pose/pose, /pose/pose/position
# rosbag_pandas.topics_from_keys(["/mbzirc_estimator/imm/state/pose/pose/position/x"])

### end of tutorial






# bag = rosbag.Bag('rosbags/2019-12-02-17-49-42.bag')
#
# dev = {'secs' : [], 'devx' : [], 'devy' : [], 'devz' : []}
#
#
# for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/ekf/state']):
#     secs = msg.header.stamp.secs + (msg.header.stamp.nsecs / 1000000000)
#     dev['secs'].append(secs)
#     m = np.asarray(msg.pose.covariance)
#     m = m.reshape(6,6)
#     diag = np.diagonal(m)
#     print(math.sqrt(diag[0]))
#     dev['devx'].append(math.sqrt(diag[0]))
#     dev['devy'].append(math.sqrt(diag[1]))
#     dev['devz'].append(math.sqrt(diag[2]))
#
# plt.subplot(3, 1, 1)
# plt.plot(dev['secs'], dev['devx'], '.-', c="g")
# plt.title('Single Model: Deviance in x,y,z vs. Time')
# plt.ylabel('Deviance x [m]')
#
# plt.subplot(3, 1, 2)
# plt.plot(dev['secs'], dev['devy'], '.-', c="g")
# plt.ylabel('Deviance y [m]')
#
# plt.subplot(3, 1, 3)
# plt.plot(dev['secs'], dev['devz'], '.-', c="g")
# plt.ylabel('Deviance z [m]')
#
# plt.xlabel('Time [s]')
#
# plt.show()




#
# data = {'secs' : [], 'nsecs' : [], 'x' : [], 'y' : [], 'z' : []}
#
# for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/imm/state']):
#     data['secs'].append(msg.header.stamp.secs)
#     data['nsecs'].append(msg.header.stamp.nsecs)
#     data['x'].append(msg.pose.pose.position.x)
#     data['y'].append(msg.pose.pose.position.y)
#     data['z'].append(msg.pose.pose.position.z)
#
# df = pd.DataFrame(data)
#
# meas_err = {'secs' : [], 'errimm' : []}
# data_err = {'secs' : [], 'errimm' : []}
#
# for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/imm/evaluation']):
#     secs = msg.header.stamp.secs + (msg.header.stamp.nsecs / 1000000000)
#     data_err['secs'].append(secs)
#     data_err['errimm'].append(msg.estimator_error)
#     meas_err['secs'].append(secs)
#     meas_err['errimm'].append(msg.measurement_error)
#
# data_errs = {'secs' : [], 'errimm' : []}
#
# for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/ekf/evaluation']):
#     secs = msg.header.stamp.secs + (msg.header.stamp.nsecs / 1000000000)
#     data_errs['secs'].append(secs)
#     data_errs['errimm'].append(msg.estimator_error)
#
#
# scat = plt.scatter(data_err['secs'], data_err['errimm'], c="b", marker="x", label="IMM Error")
# scat = plt.scatter(data_errs['secs'], data_errs['errimm'], c="g", marker="x", label="Error Single Model")
# plt.ylabel('Error [m]')
# plt.xlabel('Time [s]')
# plt.legend()
# plt.title('Error of state estimate with regards to groundtruth')
# plt.show()
#
#

#
# ximm = []
# yimm = []
# zimm = []
#
# xs = []
# ys = []
# zs = []
#
# xg = []
# yg = []
# zg = []
#
# for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/imm/state']):
#     if(len(ximm) < 10000):
#         ximm.append(msg.pose.pose.position.x)
#         yimm.append(msg.pose.pose.position.y)
#         zimm.append(msg.pose.pose.position.z)
#     else:
#         break
#
# for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/ekf/state']):
#     if(len(xs) < 10000):
#         xs.append(msg.pose.pose.position.x)
#         ys.append(msg.pose.pose.position.y)
#         zs.append(msg.pose.pose.position.z)
#     else:
#         break
#
# for topic, msg, t in bag.read_messages(topics=['/target/groundtruth/path']):
#     if(len(xg) < 10000000):
#         xg.append(msg.poses[0].pose.position.x)
#         yg.append(msg.poses[0].pose.position.y)
#         zg.append(msg.poses[0].pose.position.z)
#     else:
#         break
#
# # fig = plt.figure()
# # ax1 = fig.add_subplot(111)
#
# fig = plt.figure()
# ax = plt.axes(projection="3d")
# ax.scatter3D(ximm, yimm, zimm, c='b', marker="x", label="IMM State Estimates")
# ax.scatter3D(xs, ys, zs, c='g', marker="^", label="Single Model{ConstAcc} State Estimates")
# ax.scatter3D(xg, yg, zg, c='r', marker="o", label="Groundtruth");
#
# plt.legend()
# # plt.show()
#
# bag.close()
