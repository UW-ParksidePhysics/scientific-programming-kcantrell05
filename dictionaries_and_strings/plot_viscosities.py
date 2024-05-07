import matplotlib.pyplot as plt
import numpy as np

def parse_viscosity_data(file_name):
    viscosity_data = {}
    with open(file_name, 'r') as file:
        for line in file:
            name, C, T_knot, mu_knot = line.strip().split()
            viscosity_data[name] = {'C': float(C), 'T_knot': float(T_knot), 'mu_knot': float(mu_knot)}
    return viscosity_data

def calculate_viscosity(temperature, gas, viscosity_data):
    data = viscosity_data[gas]
    mu_knot = data['mu_knot']
    T_knot = data['T_knot']
    C = data['C']
    mu = mu_knot * ((T_knot - C) / (temperature + C)) * ((temperature / T_knot) ** 1.5)
    return mu

if __name__ == '__main__':
    # Parse viscosity data
    viscosity_data = parse_viscosity_data('viscosity_of_gases.dat')

    # Plot mu(T) for air, carbon dioxide, and hydrogen
    temperatures = np.linspace(223, 373, 100)
    gases = ['air', 'carbon_dioxide', 'hydrogen']

    plt.figure(figsize=(10, 6))
    for gas in gases:
        viscosity_values = [calculate_viscosity(T, gas, viscosity_data) for T in temperatures]
        plt.plot(temperatures, viscosity_values, label=gas)

    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity (mu)')
    plt.title('Viscosity vs Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()

