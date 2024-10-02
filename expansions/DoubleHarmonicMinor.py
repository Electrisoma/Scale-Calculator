"""
Double Harmoninc Minor Key Signature Calculator - Calculates a double harmonic minor key signature by how many sharps or flats it has
"""

scalename = 'Double Harmonic Minor'

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
  print(f"{colors.LG}1.Double Harmonic Minor{colors.END}")
  print(f"{colors.LG}2.Locrian Dominant #6{colors.END}")
  print(f"{colors.LG}3.Ionian #2 #5{colors.END}")
  print(f"{colors.LG}4.Locrian bb3 bb7{colors.END}")
  print(f"{colors.LG}5.Double Harmonic Major{colors.END}")
  print(f"{colors.LG}6.Lydian #2 #6{colors.END}")
  print(f"{colors.LG}7.Ultraphrygian{colors.END}")

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
            print(f"{colors.LG}{colors.BOLD}>>Double Harmonic Minor{colors.END}")
          if choice == '2':
            print(f"{colors.LG}{colors.BOLD}>>Locrian Dominant #6{colors.END}")
          if choice == '3':
            print(f"{colors.LG}{colors.BOLD}>>Ionian #2 #5{colors.END}")
          if choice == '4':
            print(f"{colors.LG}{colors.BOLD}>>Locrian bb3 bb7{colors.END}")
          if choice == '5':
            print(f"{colors.LG}{colors.BOLD}>>Double Harmonic Major{colors.END}")
          if choice == '6':
            print(f"{colors.LG}{colors.BOLD}>>Lydian #2 #6{colors.END}")
          if choice == '7':
            print(f"{colors.LG}{colors.BOLD}>>Ultraphrygian{colors.END}")

          if firstPrompt == '1':
            inp = int(input(f"{colors.R}>Enter number of sharps(>2): {colors.END}"))
          elif firstPrompt == '2':
            inp = int(input(f"{colors.R}>Enter number of flats(>2): {colors.END}"))

          if inp == 0: #preventing some weird stuff
            inp = 1
          if inp & 1: #circle of fifths calculator
            flats = int(inp) + 1
          else:
            flats = int(inp) - 3

        except ValueError:
             print(invalid)
             continue

        if choice == '1': #double harm minor
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-2)
            newscale = list(scaleshifter)
            newscale.pop(-2)
            newscale.pop(1)
            newscale.pop(3)
            newscale.pop(3)
            newscale.pop(6)
            return newscale        

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Double Harmonic Minor" + f"{colors.END}")
        elif choice == '2': #loc dom #6
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-4)
            newscale = list(scaleshifter)
            newscale.pop(-1)
            newscale.pop(2)
            newscale.pop(2)
            newscale.pop(5)
            newscale.pop(5)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Locrian Dominant #6" + f"{colors.END}")
        elif choice == '3': #ion #2 #5
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-5)
            newscale = list(scaleshifter)
            newscale.pop(1)
            newscale.pop(1)
            newscale.pop(4)
            newscale.pop(4)
            newscale.pop(6)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Ionian #2 #5" + f"{colors.END}")
        elif choice == '4': #loc bb3 bb7
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-8)
            newscale = list(scaleshifter)
            newscale.pop(-2)
            newscale.pop(-1)
            newscale.pop(3)
            newscale.pop(3)
            newscale.pop(5)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Locrian bb3 bb7" + f"{colors.END}")
        elif choice == '5': #Double harm major
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-9)
            newscale = list(scaleshifter)
            newscale.pop(-2)
            newscale.pop(2)
            newscale.pop(2)
            newscale.pop(4)
            newscale.pop(6)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Double Harmonic Major" + f"{colors.END}")      
        elif choice == '6': #lydian #2 #6
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-10)
            newscale = list(scaleshifter)
            newscale.pop(-3)
            newscale.pop(1)
            newscale.pop(1)
            newscale.pop(3)
            newscale.pop(5)
            return newscale
 
          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Lydian #2 #6" + f"{colors.END}")          
        elif choice == '7': #ultraphrygian
          def shiftscale(scale,flats):
            scaleshifter = deque(scale)
            scaleshifter.rotate(flats-13)
            newscale = list(scaleshifter)
            newscale.pop(-2)
            newscale.pop(-1)
            newscale.pop(2)
            newscale.pop(4)
            newscale.pop(4)
            return newscale 

          print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
          print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Ultraphrygian" + f"{colors.END}")   
    else:
        print(invalid)
