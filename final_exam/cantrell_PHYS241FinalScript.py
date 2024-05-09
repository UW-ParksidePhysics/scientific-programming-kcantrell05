import numpy as np
import matplotlib.pyplot as plt
from equations_of_state import 

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


if __name__ == "__main__":
  file_name = "Si.Fd-3m.GGA-PBE.volume_energies.dat"
  chemical_symbol, symmetry_symbol, exchange_acronym = parse_file_name(file_name)
  print("Chemical Symbol:", chemical_symbol)
  print("Symmetry Symbol:", symmetry_symbol)
  print("Exchange-Correlation Acronym:", exchange_acronym)
  
  file_path = "final_exam/Si.Fd-3m.GGA-PBE.volume_energies.dat" 
  data_array = read_data_from_file(file_path)
  print("Data Array:")
  print(data_array)



