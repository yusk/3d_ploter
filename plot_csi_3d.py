from channel_state_information import ChannelStateInformation
import sys
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np


def get_command_line_args():
    return sys.argv


def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data


args = get_command_line_args()
if len(args) > 3:
    json_filepath = args[1]
    kind = args[2]
    limit_num = int(args[3])
else:
    print("python plot_csi_3d.py [json_filepath] [kind] [limit_num]")
    exit()

data = load_json(json_filepath)

x, y = np.meshgrid(
    np.arange(1, 30 + 1), np.arange(1, min(len(data), limit_num) + 1))

z = [[], [], []]

if kind == "power":
    for csi_dict in data[:limit_num]:
        csi = ChannelStateInformation(csi_dict)
        z[0].append(csi.powers[0])
        z[1].append(csi.powers[1])
        z[2].append(csi.powers[2])
elif kind == "phase":
    for csi_dict in data[:limit_num]:
        csi = ChannelStateInformation(csi_dict)
        z[0].append(csi.phases[0])
        z[1].append(csi.phases[1])
        z[2].append(csi.phases[2])

fig = plt.figure(figsize=(16, 6))
ax = fig.add_subplot(131, projection='3d')
ax.plot_wireframe(x, y, z[0], cmap=cm.coolwarm)
ax = fig.add_subplot(132, projection='3d')
ax.plot_wireframe(x, y, z[1], cmap=cm.coolwarm)
ax = fig.add_subplot(133, projection='3d')
ax.plot_wireframe(x, y, z[2], cmap=cm.coolwarm)
plt.show()
