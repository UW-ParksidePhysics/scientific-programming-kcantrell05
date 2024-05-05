def parse_constants_file(constants.txt):
  infile = open(constants.txt, 'r')
  constants = {}
  for line in infile:
    words = line.split()
    constant = float(words[-1])

    if len(words[:-1]) == 2:
      substance = words[0] + ' ' + words[1]
    else:
        substance = words[0]

    constants[substance] = constant
  infile.close()
  return constants
    

if __name__ == '__main__':
  constants = parse_constants_file('constants.txt')
  print(constants)