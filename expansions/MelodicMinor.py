"""
Melodic Minor Key Signature Calculator - Calculates a melodic minor key signature by how many sharps it has
"""

scalename = 'Melodic Minor'

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
  print(f"{colors.LG}1.Melodic Minor{colors.END}")
  print(f"{colors.LG}2.Dorian b2{colors.END}")
  print(f"{colors.LG}3.Lydian Augmented{colors.END}")
  print(f"{colors.LG}4.Lydian Dominant{colors.END}")
  print(f"{colors.LG}5.Mixolydian b6{colors.END}")
  print(f"{colors.LG}6.Locrian ♮ 2{colors.END}")
  print(f"{colors.LG}7.Super Locrian{colors.END}")

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
            print(f"{colors.LG}{colors.BOLD}>>Harmonic Minor{colors.END}")
          if choice == '2':
            print(f"{colors.LG}{colors.BOLD}>>Dorian b2{colors.END}")
          if choice == '3':
            print(f"{colors.LG}{colors.BOLD}>>Lydian Augmented{colors.END}")
          if choice == '4':
            print(f"{colors.LG}{colors.BOLD}>>Lydian Dominant{colors.END}")
          if choice == '5':
            print(f"{colors.LG}{colors.BOLD}>>Mixolydian b6{colors.END}")
          if choice == '6':
            print(f"{colors.LG}{colors.BOLD}>>Locrian ♮ 2{colors.END}")
          if choice == '7':
            print(f"{colors.LG}{colors.BOLD}>>Super Locrian{colors.END}")

          if firstPrompt == '1':
            inp = int(input(f"{colors.R}>Enter number of sharps(>2): {colors.END}"))
          elif firstPrompt == '2':
            inp = int(input(f"{colors.R}>Enter number of flats(>2): {colors.END}"))

          if inp == 0: #prevents some weird stuff
            inp = 1

          if inp & 1: #circle of fifths calculator
            flats = int(inp) + 1
          else:
            flats = int(inp) - 3

        except ValueError:
             print(invalid)
             continue

        if choice == '1': #melodic minor
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-2)
            newscale = list(scaleshifter)
            newscale.pop(-2)
            newscale.pop(1)
            newscale.pop(3)
            newscale.pop(4)
            newscale.pop(5)
            return newscale        

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Melodic Minor" + f"{colors.END}")
        elif choice == '2': #dor b2
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-4)
            newscale = list(scaleshifter)
            newscale.pop(-1)
            newscale.pop(2)
            newscale.pop(3)
            newscale.pop(4)
            newscale.pop(5)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Locrian ♮ 6" + f"{colors.END}")
        elif choice == '3': #lydian aug
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-5)
            newscale = list(scaleshifter)
            newscale.pop(-2)
            newscale.pop(1)
            newscale.pop(2)
            newscale.pop(3)
            newscale.pop(4)            
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Augmented Major" + f"{colors.END}")
        elif choice == '4': #lydian dom
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-7)
            newscale = list(scaleshifter)
            newscale.pop(-1)
            newscale.pop(1)
            newscale.pop(2)
            newscale.pop(3)
            newscale.pop(5)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Dorian #11" + f"{colors.END}")
        elif choice == '5': #mixo b6
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-9)
            newscale = list(scaleshifter)
            newscale.pop(-1)
            newscale.pop(1)
            newscale.pop(2)
            newscale.pop(4)
            newscale.pop(6)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Phrygian Dominant" + f"{colors.END}")          
        elif choice == '6': #loc nat 2
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-10)
            newscale = list(scaleshifter)
            newscale.pop(0)
            newscale.pop(1)
            newscale.pop(3)
            newscale.pop(5)
            newscale.pop(6)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Lydian #2" + f"{colors.END}")          
        elif choice == '7': #super loc
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-13)
            newscale = list(scaleshifter)
            newscale.pop(-1)
            newscale.pop(2)
            newscale.pop(4)
            newscale.pop(5)
            newscale.pop(6)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Altered Diminished" + f"{colors.END}")   
    else:
        print(invalid)
