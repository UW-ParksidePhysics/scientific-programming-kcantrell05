import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation









def update_figure(frame):
  # update the plot corve y-data for each frame
  plot_curve.set_ydata(temperatures[frame])
  return plot curve


if __name__ = '__main__':
  # Choose backend software for graphing
  matplotlib.use('TkAgg')

# Simulation parameters
thermal_diffusivity = 1.e-6
oscillation_period = 