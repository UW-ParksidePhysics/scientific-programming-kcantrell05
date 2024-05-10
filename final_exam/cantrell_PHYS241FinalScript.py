import numpy as np
import matplotlib.pyplot as plt
from calculate_bivariate_statistics import compute_bivariate_statistics
from calculate_quadratic_fit import compute_quadratic_coefficients
from scipy import stats
from scipy import constants
from equations_of_state import fit_eos
from generate_matrix import generate_matrix


# PART 1: Fit an Equation of State


def parse_file_name(file_name):

  file_name = file_name.replace(".dat", "")

  parts = file_name.split('.')

  chemical_symbol = parts[0]  
  symmetry_symbol = parts[1]  
  exchange_acronym = parts[2]  

  return chemical_symbol, symmetry_symbol, exchange_acronym
  

def read_data_from_file(file_path):
  
      try:
        data = np.loadtxt(file_path).transpose()
        return data
      except OSError as err:
        print(f'Error: {err}')
      return None

def compute_quadratic_coefficients(data):
  """
  Calculate quadratic coefficients for a given dataset.
  :param data: ndarray, shape(2,M)
  :return: quadratic_coefficients: ndarray, shape(3,)
  """
  quadratic_coefficients = np.polyfit(data[0], data[1], 2)
  ordered_quadratic_coefficients = [quadratic_coefficients[-1], quadratic_coefficients[1], quadratic_coefficients[0]]

  return quadratic_coefficients

def fit_eos(volumes, energies, quadratic_coefficients, eos='vinet', number_of_points=50):

  from scipy.optimize import curve_fit

  # Dictionary holding lambda functions from current module.
  lambda_dictionary = {
      'vinet': globals()['vinet'],
  }

  minimum_volume = np.amin(volumes)
  maximum_volume = np.amax(volumes)

  quadratic_axis_of_symmetry = -quadratic_coefficients[1] / (2 * quadratic_coefficients[2])
 
  quadratic_minimum = -quadratic_coefficients[1] ** 2 / (4 * quadratic_coefficients[2]) + quadratic_coefficients[0]
 
  quadratic_bulk_modulus = 2. * quadratic_coefficients[2] / quadratic_axis_of_symmetry

  bulk_modulus_derivative = 3.7

  initial_parameters = [quadratic_minimum, quadratic_bulk_modulus, bulk_modulus_derivative, quadratic_axis_of_symmetry]

  eos_parameters, eos_covariances = curve_fit(lambda_dictionary[eos.lower()], volumes, energies, p0=initial_parameters, method='trf') 
  
  fit_curve_volumes = np.linspace(minimum_volume, maximum_volume, num=number_of_points)
  eos_fit_curve = lambda_dictionary[eos.lower()](fit_curve_volumes, eos_parameters[0], eos_parameters[1], eos_parameters[2], eos_parameters[3])

  return eos_fit_curve, eos_parameters


def vinet(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):

  k0pm1 = bulk_modulus_derivative - 1  # K_0' - 1
  k0pm1_squared = np.power(k0pm1, 2)
  reduced_volume_lengths = np.cbrt(volumes / equilibrium_volume)

  exponential_argument = -1.5 * k0pm1 * (reduced_volume_lengths - 1.)
  try:
      exponential_factor = np.exp(exponential_argument)
      vinet_eos = equilibrium_energy + (2. * bulk_modulus * equilibrium_volume / k0pm1_squared) * (2. - (5. + 3. * reduced_volume_lengths * k0pm1 - 3 * bulk_modulus_derivative) * exponential_factor)
  except:
      vinet_eos = equilibrium_energy +(2. * bulk_modulus * equilibrium_volume / k0pm1_squared) * (2. - (5. + 3. * reduced_volume_lengths * k0pm1 - 3 * bulk_modulus_derivative))
  return vinet_eos

def convert_units(value, from_units, to_units):
  conversion_factors = {
      ('bohr', 'angstrom'): constants.angstrom,
      ('rydberg', 'electron_volt'): constants.eV,
      ('rydberg/bohr^3', 'gigapascal'): constants.giga,
  }
  return value * conversion_factors[(from_units, to_units)]


if __name__ == "__main__":
  file_name = "Si.Fd-3m.GGA-PBE.volume_energies.dat"
  chemical_symbol, symmetry_symbol, exchange_acronym = parse_file_name(file_name)
  print("Chemical Symbol:", chemical_symbol)
  print("Symmetry Symbol:", symmetry_symbol)
  print("Exchange-Correlation Acronym:", exchange_acronym)
  
  file_path = "final_exam/Si.Fd-3m.GGA-PBE.volumes_energies.dat"
  data_array = read_data_from_file(file_path)
  print("Data Array:")
  print(data_array)
  if data_array is not None:
      stats = compute_bivariate_statistics(data_array)
      print("Statistics on the dataset:")
      print("Mean of y:", stats[0])
      print("Standard Deviation of y:", stats[1])
      print("Minimum of x:", stats[2])
      print("Maximum of x:", stats[3])
      print("Minimum of y:", stats[4])
      print("Maximum of y:", stats[5])
  else:
      print("Failed to read the data from the file.")

value_names = ['quadratic coefficient', 'linear coefficient', 'constant coefficient']
for name, value in zip(value_names, compute_quadratic_coefficients([np.linspace(-1, 1), np.linspace(-1, 1)**2])):
    print(f'{name}: {value}')  
    fit_point_number = 50
    test_energies = np.array([-2.2821*np.exp(1), -2.2829*np.exp(1), -2.2834*np.exp(1), -2.2838*np.exp(1), -2.2840*np.exp(1)])
    test_volumes = np.array([2.3923*np.exp(2), 2.4679*np.exp(2), 2.5450*np.exp(2), 2.6237*np.exp(2), 2.7040*np.exp(2)])
    starting_coefficients = np.polynomial.polynomial.polyfit(test_volumes, test_energies, 2)
    equation_of_state = ['vinet']
    figures, axes = plt.subplots(nrows=len(equation_of_state))

    for index, eos_form in enumerate(equation_of_state):
      eos, eos_parameters = fit_eos(test_volumes, test_energies, starting_coefficients, eos=eos_form, number_of_points=fit_point_number)
      axes.plot(np.linspace(10, 14, num=fit_point_number), eos)
      axes.scatter(test_volumes, test_energies)
      axes.text(12, -19, eos_form.title(), ha='center', va='center')
    plt.show()

volumes_angstrom = convert_units(test_volumes, 'bohr', 'angstrom')
energies_ev = convert_units(test_energies, 'rydberg', 'electron_volt')
eos_ev = convert_units(eos, 'rydberg', 'electron_volt')

plt.plot(volumes_angstrom, eos_ev, color='black', linestyle='-', linewidth=2)

plt.scatter(volumes_angstrom, energies_ev, color='blue', marker='o', facecolors='none', edgecolors='blue')

plt.xlabel(r'Volume ($\AA^3$/atom)')
plt.ylabel(r'Energy (eV/atom)')

x_range = np.max(volumes_angstrom) - np.min(volumes_angstrom)
y_range = np.max(energies_ev) - np.min(energies_ev)
x_pad = 0.1 * x_range
y_pad = 0.1 * y_range
plt.xlim(np.min(volumes_angstrom) - x_pad, np.max(volumes_angstrom) + x_pad)
plt.ylim(np.min(energies_ev) - y_pad, np.max(energies_ev) + y_pad)
plt.title('Equation of State Fit')


plt.tight_layout()
plt.show()
