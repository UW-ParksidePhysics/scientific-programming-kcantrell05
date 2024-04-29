import numpy as np
import matplotlib.pyplot as plt
import math

mass = 0.2  # kg
length = 0.1  # m (10 cm)
initial_angles = [np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 6]
initial_velocity = 1  # rad/s (changed from 0 to observe motion)

def conservation_of_momentum(velocity):
    return sum(velocity) * mass  # Multiply by mass to get momentum

def conservation_of_energy(angular_velocity):
    return 0.5 * mass * length**2 * angular_velocity**2

def angular_velocity(time, initial_angle):
    # Angular velocity as a function of time
    return initial_velocity * np.cos(initial_angle) * np.cos(time)

def angular_displacement(time, initial_angle):
    # Angular displacement as a function of time
    return initial_velocity * np.sin(initial_angle) * time

# Time range with higher resolution
time_points = np.linspace(0, 10 * np.pi, 1000)

# Print conservation of momentum and energy for each initial angle
for angle in initial_angles:
    v = angular_velocity(0, angle)
    e = conservation_of_energy(v)
    print(f"Initial Angle: {angle:.2f}, Conservation of Momentum: {conservation_of_momentum([v]):.2f} N·s, Conservation of Energy: {e:.2f} J")

# Create subplots for angular velocity and angular displacement
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
axs[0].set_title('Angular Velocity vs Time')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Angular Velocity (rad/s)')

axs[1].set_title('Angular Displacement vs Time')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Angular Displacement (rad)')

# Plot each initial angle separately with different colors
for i, angle in enumerate(initial_angles):
    # Calculate angular velocity and displacement
    angular_velocities = [angular_velocity(t, angle) for t in time_points]
    angular_displacements = [angular_displacement(t, angle) for t in time_points]

    # Plot angular velocity as continuous curve
    axs[0].plot(time_points, angular_velocities, label=f'Initial Angle: {angle:.2f}')

    # Plot angular displacement with checkmark pattern
    axs[1].plot(time_points, angular_displacements, label=f'Initial Angle: {angle:.2f}', linestyle='-', marker='o', markevery=50)

# Show legends
axs[0].legend()
axs[1].legend()

# Adjust layout to space out the subplots vertically
plt.subplots_adjust(hspace=0.5)

plt.tight_layout()
plt.show()
