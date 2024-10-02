"""
Harmoninc Minor Key Signature Calculator - Calculates a harmonic minor key signature by how many sharps it has
"""

scalename = 'Harmonic Major'

import sys
sys.path.append("utils")
import math
from collections import deque
from calcutils import scaleA
from calcutils import scaleB
from calcutils import invalid
from calcutils import colors
from calcutils import sourcescaleName
from calcutils import back

def scale():
  print(sourcescaleName(scalename))

  print(f"{colors.Y}select scale{colors.END}") #scales and modes
  print(f"{colors.LG}1.Harmonic Major{colors.END}")
  print(f"{colors.LG}2.Dorian b5{colors.END}")
  print(f"{colors.LG}3.Phrygian b4{colors.END}")
  print(f"{colors.LG}4.Lydian b3{colors.END}")
  print(f"{colors.LG}5.Mixolydian b2{colors.END}")
  print(f"{colors.LG}6.Lydian Augmented #2{colors.END}")
  print(f"{colors.LG}7.Locrian bb7{colors.END}")
  scale = scaleA

  while True:
    choice = input(f"{colors.LP}>Enter scale: {colors.END}")

    if choice == 'b': #back button
      back()
      break

    firstPrompt = input(f"{colors.R}>Sharps or flats(1/2): {colors.END}")

    if firstPrompt in ['1','2']:
      if firstPrompt == '1':
        scale = scaleA
      elif firstPrompt == '2':
        scale = scaleB 

    if firstPrompt == 'b': #back button
      back()
      break

    if choice in ['1','2','3','4','5','6','7']:
      try:
        if choice == '1':
          print(f"{colors.LG}{colors.BOLD}>>Harmonic Major{colors.END}")
        elif choice == '2':
          print(f"{colors.LG}{colors.BOLD}>>Dorian b2{colors.END}")
        elif choice == '3':
          print(f"{colors.LG}{colors.BOLD}>>Phrygian b4{colors.END}")
        elif choice == '4':
          print(f"{colors.LG}{colors.BOLD}>>Lydian b3{colors.END}")
        elif choice == '5':
          print(f"{colors.LG}{colors.BOLD}>>Mixolydian b2{colors.END}")
        elif choice == '6':
          print(f"{colors.LG}{colors.BOLD}>>Lydian Augmented #2{colors.END}")
        elif choice == '7':
          print(f"{colors.LG}{colors.BOLD}>>Locrian bb7{colors.END}")

        if firstPrompt == '1':
          inp = int(input(f"{colors.R}>Enter number of sharps(>1): {colors.END}"))
        elif firstPrompt == '2':
          inp = int(input(f"{colors.R}>Enter number of flats(>1): {colors.END}"))
        
        if inp == 0: #preventing some weird stuff
            inp = 1
        if inp & 1: #circle of fifths calculator
          flats = int(inp) * 4
        else:
          flats = int(inp) - 1 * 3

      except ValueError:
        print(invalid)
        continue

      if choice == '1': #harm major
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-7)
          newscale = list(scaleshifter)
          newscale.pop(1)
          newscale.pop(2)
          newscale.pop(4)
          newscale.pop(6)
          newscale.pop(6)
          return newscale        

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Harmonic Major" + f"{colors.END}")
      elif choice == '2': #dorian b2
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-9)
          newscale = list(scaleshifter)
          newscale.pop(-1)
          newscale.pop(1)
          newscale.pop(3)
          newscale.pop(5)
          newscale.pop(5)
          return newscale 

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Dorian b2" + f"{colors.END}")
      elif choice == '3': #phrygian b4
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-11)
          newscale = list(scaleshifter)
          newscale.pop(-1)
          newscale.pop(2)
          newscale.pop(4)
          newscale.pop(4)
          newscale.pop(6)            
          return newscale 

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Phrygian b4" + f"{colors.END}")
      elif choice == '4': #lydian b3
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-12)
          newscale = list(scaleshifter)
          newscale.pop(-2)
          newscale.pop(1)
          newscale.pop(3)
          newscale.pop(3)
          newscale.pop(5)
          return newscale 

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Dorian #11" + f"{colors.END}")
      elif choice == '5': #mixolydian b2
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-14)
          newscale = list(scaleshifter)
          newscale.pop(-1)
          newscale.pop(2)
          newscale.pop(2)
          newscale.pop(4)
          newscale.pop(5)
          return newscale 

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Mixolydian b2" + f"{colors.END}")          
      elif choice == '6': #lydian aug #2
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-15)
          newscale = list(scaleshifter)
          newscale.pop(1)
          newscale.pop(1)
          newscale.pop(3)
          newscale.pop(4)
          newscale.pop(6)
          return newscale 

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Lydian Augmented #2" + f"{colors.END}")          
      elif choice == '7': #locrian bb7
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-18)
          newscale = list(scaleshifter)
          newscale.pop(-2)
          newscale.pop(-1)
          newscale.pop(2)
          newscale.pop(3)
          newscale.pop(5)
          return newscale 

        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Locrian bb7" + f"{colors.END}")   
    else:
      print(invalid)
