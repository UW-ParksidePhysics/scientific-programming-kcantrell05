
# My Python project is Newton's Cradle.
# The functions listed are to show the elements of Newton's Cradle in action.
# Displayed currently are two graphs showing the relationships between angular velocity and displacement over time.
# The main physical principle in Newton's Cradle is elastic collisions.
# This is observed through the conservation of momentum and energy.


import numpy as np
import matplotlib.pyplot as plt

# mass = 1
# def conservation_of_momentum(velocity, initial_velocity=0, mass=1):
#   return sum(velocity)


# def positon_of_ball(angle, length=10):
#   return length * math.sin(angle)

# def angular_momentum(angular_velocity, length, mass):
#   return mass * length * angular_velocity

# def angular_velocity(time, initial_angle=math.pi /6, initial_angular_velocity=0.5):
#   return initial_angular_velocity * math.cos(initial_angle) * math.cos(time)

# velocity = [float(x) for x in input("Enter the velocity (comma-separated): ").split(",")]
# print("Conservation of Momentum:", conservation_of_momentum(velocity))
# print("Position of Ball:", positon_of_ball(math.pi /6, 10))
# print("Angular Momentum:", angular_momentum(0.5, 10, 1))
# print("Angular Velocity:", angular_velocity(1, math.pi /6, 0.5))

# time_points = np.linspace(0, 10, 100)

# angular_velocities = [angular_velocity(t) for t in time_points]


# plt.plot(time_points, angular_velocities)
# plt.xlabel('Time (s)')
# plt.ylabel('Angular Velocity (rad/s)')
# plt.title('Angular Velocity vs Time')
# plt.grid(True)
# plt.show()


def conserve_momentum(velocity, mass):
    return sum(velocity) * mass  # Multiply by mass to get momentum


def conserve_energy(angular_velocity, mass, length):
    return 0.5 * mass * length ** 2 * angular_velocity ** 2


def calculate_angular_velocity(time, initial_angle, resonant_frequency):
    # Angular velocity as a function of time
    return -initial_angle * resonant_frequency * np.sin(resonant_frequency * time)


def calculate_angular_position(time, initial_angle, resonant_frequency):
    # Angular displacement as a function of time
    return initial_angle * np.cos(resonant_frequency * time)


def simulate_newtons_cradle():
    bob_mass = 0.2  # kg
    pendulum_length = 0.1  # m (10 cm)
    standard_gravity = 9.8   # m/s/s
    pendulum_frequency = np.sqrt(standard_gravity/pendulum_length)
    pendulum_period = 2 * np.pi / pendulum_frequency
    number_of_periods = 4
    initial_angles = [np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 6]
    initial_velocity = 1  # rad/s (changed from 0 to observe motion)

    # Time range with higher resolution
    time_points = np.linspace(0, number_of_periods * pendulum_period, 1000)

    # Print conservation of momentum and energy for each initial angle
    for angle in initial_angles:
        v = calculate_angular_velocity(time_points[0], angle, pendulum_frequency)
        e = conserve_energy(v, bob_mass, pendulum_length)
        print(
            f"Initial Angle: {angle:.2f}, Conservation of Momentum: {conserve_momentum([v], bob_mass):.2f} N·s, Conservation of Energy: {e:.2f} J")

    # Create subplots for angular velocity and angular displacement
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Angular Velocity (rad/s)')
    axs[0].axhline()

    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Angular Displacement (rad)')
    axs[1].axhline()

    # Plot each initial angle separately with different colors
    for i, angle in enumerate(initial_angles):
        # Calculate angular velocity and displacement
        angular_velocities = [calculate_angular_velocity(t, angle, pendulum_frequency) for t in time_points]
        angular_displacements = [calculate_angular_position(t, angle, pendulum_frequency) for t in time_points]

        # Plot angular velocity as continuous curve
        axs[0].plot(time_points, angular_velocities, label=f'Initial Angle: {angle:.2f}')

        # Plot angular displacement with checkmark pattern
        axs[1].plot(time_points, angular_displacements, label=f'Initial Angle: {angle:.2f}', linestyle='-', marker='o',
                    markevery=50)

    # Show legends
    axs[0].legend(title=r'$\theta_0$')

    # Add an overall title
    fig.suptitle('Angular Velocity and Displacement in Newtons Cradle')

    # Adjust layout to space out the subplots vertically
    plt.subplots_adjust(hspace=1.5)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    simulate_newtons_cradle()

