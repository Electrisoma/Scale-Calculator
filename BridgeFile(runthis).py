"""
Key Signature Calculator Framework - Bridges all associated files
"""

#total amount of scales 
#y = 2(x(7^2(12)))
#x = total number of files in expansions

import sys
sys.path.append("utils")
from calcutils import invalid
from calcutils import colors
from pathlib import Path

while True:
  IMajor = Path('expansions/Major.py')
  HarmMinor = Path('expansions/HarmonicMinor.py')
  HarmMajor = Path('expansions/HarmonicMajor.py')
  MeloMinor = Path('expansions/MelodicMinor.py')
  DHarmMinor = Path('expansions/DoubleHarmonicMinor.py')
  scales = [] #scale list

  if IMajor.is_file():
    scales.append('--Major')
    from expansions import Major
  if HarmMinor.is_file():
    scales.append('--Harmonic Minor')
    from expansions import HarmonicMinor
  if HarmMajor.is_file():
    scales.append('--Harmonic Major')
  if MeloMinor.is_file():
    scales.append('--Melodic Minor')
    from expansions import MelodicMinor
  if DHarmMinor.is_file():
    scales.append('--Double Harmonic Minor')
    from expansions import DoubleHarmonicMinor

  #scale list print
  print(f"{colors.Y}select source scale{colors.END}")
  print(f"{colors.LG}" + '\n'.join(scales) + f"{colors.END}")
  print(f"{colors.LR}press (b) to go back{colors.END}")
  source = input(f"{colors.R}>Enter source scale: {colors.END}")

  if source in ['1','2','3','4','5']:
    if source == '1':
      if IMajor.is_file():
        Major.scale()
      else:
        print(invalid)

    elif source == '2':
      if HarmMinor.is_file():
        HarmonicMinor.scale()
      else:
        print(invalid)

    elif source == '3':
      if HarmMajor.is_file():
        HarmonicMinor.scale()
      else:
        print(invalid)

    elif source == '4':
      if MeloMinor.is_file():
        MelodicMinor.scale()
      else:
        print(invalid)

    elif source == '5':
      if DHarmMinor.is_file():
        DoubleHarmonicMinor.scale()
      else:
        print(invalid)

  else:
    print(invalid)
