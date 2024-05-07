def parse_constants_file(file_name):
  constants = {}
  with open(file_name, 'r') as infile:
      for line in infile:
          words = line.strip().split()
          try:
              constant = float(words[-1])
          except ValueError:
              print(f"Ignoring line: {line.strip()} (last word is not a number)")
              continue

          if len(words) == 3:
              substance = words[0] + ' ' + words[1]
          else:
              substance = words[0]

          constants[substance] = constant
  return constants

if __name__ == '__main__':
  constants = parse_constants_file('constants.txt')
  print(constants)
