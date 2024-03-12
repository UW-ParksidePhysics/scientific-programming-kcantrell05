# y_0 = initial position
# v_0 = initial velocity
# t = time since release

initial_position = 15 # m
initial_velocity = 3 # m/s^
gravity = 9.8 # m/s^2
time_since_release = 0.6 # s
y = initial_position + initial_velocity*time_since_release - 0.5*gravity*time_since_release**2

def y_position(initial_position, initial_velocity, time_since_release):
    y = initial_position + initial_velocity*time_since_release - 0.5*gravity*time_since_release**2
    return y

print(f'The initial position is {initial_position} m')
print(f'The initial velocity is {initial_velocity} m/s')
print(f'The time since release is {time_since_release} s')
print(f'Freefall position: {y: .3f} m')
