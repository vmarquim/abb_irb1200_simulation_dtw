import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from dtw import *


def dtw_plot_3d(reference_data_frame, query_data_frame):

    x1 = reference_data_frame['x'].to_numpy()
    y1 = reference_data_frame['y'].to_numpy()
    z1 = reference_data_frame['z'].to_numpy()

    x2 = query_data_frame['x'].to_numpy()
    y2 = query_data_frame['y'].to_numpy()
    z2 = query_data_frame['z'].to_numpy()

    fig = plt.figure()
    ax  = fig.add_subplot(111, projection = '3d')


    ax.plot3D(x1, y1, z1, color="blue", label="Simulated Trajectory")
    ax.plot3D(x2, y2, z2, color="red", label="Theoretical Trajectory")

    df1 = np.vstack((x1, y1, z1)).reshape(-1, 3)
    df2 = np.vstack((x2, y2, z2)).reshape(-1, 3)

    alignment = dtw(df1, df2, keep_internals=True)

    alignment.plot("threeway")

    for i, j in zip(alignment.index1, alignment.index2):
        ax.plot3D(np.array([x1[i], x2[j]]), np.array([y1[i], y2[j]]), np.array([z1[i], z2[j]]), linestyle="dashed", linewidth=0.3, color="gray")
        ax.scatter3D(np.array([x1[i], x2[j]]), np.array([y1[i], y2[j]]), np.array([z1[i], z2[j]]), color="gray")

    ax.set_title("DTW - Normalised Distance: %s" % round(alignment.normalizedDistance, 2))
    ax.set_xlabel("x in meters")
    ax.set_ylabel("y in meters")
    ax.set_zlabel("z in meters")
    ax.legend()
    plt.show()


def plot_dtw_3d_test():

    # Test data
    n1 = 100
    x1 = np.linspace(0, 5, n1)
    y1 = x1*x1
    z1 = np.full_like(x1, 0)

    n2 = n1
    x2 = np.linspace(0, 5, n2)
    y2 = x2*x2
    z2 = np.full_like(x2, 3)

    fig = plt.figure()
    ax  = fig.add_subplot(111, projection = '3d')

    ax.plot3D(x1, y1, z1, color="red", label="Simulated Trajectory")
    ax.plot3D(x2, y2, z2, color="blue", label="Theoretical Trajectory")

    df1 = np.vstack((x1, y1, z1)).reshape(-1, 3)
    df2 = np.vstack((x2, y2, z2)).reshape(-1, 3)

    # print(df1.shape)
    # print(df2.shape)

    alignment = dtw(df1, df2, keep_internals=True)

    # print(alignment.index1)
    # print(alignment.index2)

    # print(x1)

    alignment.plot("threeway")

    print(alignment.__dict__)

    for i, j in zip(alignment.index1, alignment.index2):
        # print(i, j)
        ax.plot3D(np.array([x1[i], x2[j]]), np.array([y1[i], y2[j]]), np.array([z1[i], z2[j]]), linestyle="dashed", linewidth=0.3, color="gray")
        ax.scatter3D(np.array([x1[i], x2[j]]), np.array([y1[i], y2[j]]), np.array([z1[i], z2[j]]), color="gray")

    ax.set_title("DTW - Normalised Distance: %s" % round(alignment.normalizedDistance, 2))
    ax.set_xlabel("x in meters")
    ax.set_ylabel("y in meters")
    ax.set_zlabel("z in meters")

    ax.legend()

    plt.show()


if __name__ == "__main__":
    plot_dtw_3d_test()