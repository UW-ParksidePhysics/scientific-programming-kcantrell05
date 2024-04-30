import matplotlib
import matplotlib.pyplot as plt


def calculate_surface_gravity(planet_massm planet_radius):

planet_data = {'venus': {'gravity':8.9, 'mass': 4.87e24, 'diameter': 12_104e3}, 'earth': {'gravity': 9.8, 'mass': 5.97e24, 'diameter': 12_756e3 }, 'mars': {'gravity': 3.7, 'mass': 0.642e24, 'diameter': 6_792e3 }}


#for index, item in enumerate(planet_data.values


#plt.plot(gravitational_accelerations, marker='o')
#plt.show

if __name__ = '__main__':
  #print(calculate_surface_gravity(5.97e24, 12_756e3 / 2))
for index, planet in enumerate(planet_data):
    planet_dictionary = planet_data[planet]
    standard_acceleration = planet_dictionary['gravity']
    #plt.text(index, standard_acceleration, planet)
    planet_names.append(planet.capitalize())
    calculated_acceleration = calculate_surface_gravity(planet_dictionary['mass'], planet_dictionary['diameter']/2)