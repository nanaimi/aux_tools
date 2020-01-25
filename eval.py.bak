import rosbag
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
import math

bag = rosbag.Bag('rosbags/2019-12-02-17-49-42.bag')

dev = {'secs' : [], 'devx' : [], 'devy' : [], 'devz' : []}




for topic, msg, t in bag.read_messages(topics=['/mbzirc_estimator/ekf/state']):
    secs = msg.header.stamp.secs + (msg.header.stamp.nsecs / 1000000000)
    dev['secs'].append(secs)
    m = np.asarray(msg.pose.covariance)
    m = m.reshape(6,6)
    diag = np.diagonal(m)
    print(math.sqrt(diag[0]))
    dev['devx'].append(math.sqrt(diag[0]))
    dev['devy'].append(math.sqrt(diag[1]))
    dev['devz'].append(math.sqrt(diag[2]))

plt.subplot(3, 1, 1)
plt.plot(dev['secs'], dev['devx'], '.-', c="g")
plt.title('Single Model: Deviance in x,y,z vs. Time')
plt.ylabel('Deviance x [m]')

plt.subplot(3, 1, 2)
plt.plot(dev['secs'], dev['devy'], '.-', c="g")
plt.ylabel('Deviance y [m]')

plt.subplot(3, 1, 3)
plt.plot(dev['secs'], dev['devz'], '.-', c="g")
plt.ylabel('Deviance z [m]')

plt.xlabel('Time [s]')

plt.show()





















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

