import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def setup_location_coordinates (num):
    x = np.random.rand(num)
    y = np.random.rand(num)
    z = np.random.rand(num)

    return [[float(x[i]), float(y[i]), float(z[i])] for i in range(num)]

location_coordinates = setup_location_coordinates(10)

print(location_coordinates)

def visualise_3d_coordinates(location_coordinates, provided_path = None) :
    fig = plt.figure