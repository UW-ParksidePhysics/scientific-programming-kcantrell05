# define kinetic energy function
# define potential energy function
# import height and velocity functions of time from freefall_kinematics
# define the array of times from 0 to 2 v_0/g
# plot the energies verus time
# predefine mass and initial velocity
import numpy as np
from freefall_kinematics import height, velocity


def kinetic_energy(velocity, mass):
  return 0.5 * mass * velocity ** 2


def potential_energy(height, mass, gravitational_acceleration):
  return mass * gravitational_acceleration * height


def calculate_energies(mass, initial_velocity, number_of_times, gravitational_acceleration=9.8):
  end_time = 2 * initial_velocity / gravitational_acceleration
  times = np.linspace(0, end_time, 100)
  heights = height(times, initial_height, initial_velocity, gravitational_acceleration)
  velocities = velocity(times, initial_velocity, gravitational_acceleration)
  kinetic_energies = kinetic_energy(velocities, mass)
  potential_energies = potential_energy(heights, mass, gravitational_acceleration=gravitational_acceleration)
  total_energies = kinetic_energies + potential_energies
  return [times, kinetic_energies, potential_energies, total_energies]


def plot_energies(times, kinetic_energies, potential_energies, total_energies):
  import matplotlib.pyplot as plt
  plt.plot(times, kinetic_energies, label='$K(t)$')
  plt.plot(times, potential_energies, label='$P(t)$')
  plt.plot(times, total_energies, label='$E(t)$')
  plt.xlabel('$t$ (s)')
  plt.ylabel('$E, K, P$ (J)')
  plt.show()
  return


if __name__ == '__main__':
  object_mass = 1.
  starting_height = 1.
  starting_velocity = 1.
  time_sample_number = 100
  times_and_energies = calculate_energies(object_mass, starting_height, starting_velocity, time_sample_number)
  plot_energies(times_and_energies[0], times_and_energies[1], times_and_energies[2], times_and_energies[3])







